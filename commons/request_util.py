# -*- encoding：utf-8 -*-
# @Author: Kurosaki
# @Date Time: 2022/9/7 22:46
# @Filename: request_util
# @Description: 标准化yaml测试用例
import json
import logging
import re
from io import StringIO

import jsonpath
import requests
import yaml

from commons.assert_util import assert_result
from commons.global_args import load_ini
from commons.yaml_util import write_yaml
from hotloads.debug_util import DebugTalk

# 根据文件名获得日志对象
logger = logging.getLogger(__name__)


class RequestUtil:
    sess = requests.session()

    # 标准化yaml测试用例
    def standard_yaml(self,caseinfo):#(self, caseinfo, base_url):
        # 打印日志
        # logger.info("aaaa")

        # 在请求之前调用热加载，通过反射使yaml能调用python里的函数
        yaml_str = yaml.dump(caseinfo)  # 把字典转换成字符串,建议使用
        # yaml_str = json.dumps(caseinfo)  # 把字典转换成字符串
        yaml_str = self.replace_hotload(yaml_str)
        caseinfo = yaml.safe_load(StringIO(yaml_str))  # 字符转换成字符串文件流再转成字典，提取的是整型就是整型，字符串就是字符串

        case_keys = caseinfo.keys()
        # print(case_keys)
        # 如果后者{}的超集set（）返回True
        if set(case_keys).issuperset({'feature','story', 'title', 'request', 'validate'}):
            request_keys = caseinfo['request'].keys()
            # print(request_keys)
            # 判断request中必须有method，url
            if set(request_keys).issuperset({'method', 'url'}):
                # print('用例格式正确')
                # 处理url
                # # 判断yaml中的url是否以http开头,不是的话传入base_url
                # if "http" not in caseinfo["request"]["url"]:
                #     caseinfo['request']['url'] = base_url + caseinfo['request']['url']
                # print(caseinfo['request']['url'])

                # 加入日志
                logger.info("----------测试用例请求开始----------")
                logger.info("用例标题：%s" % caseinfo["title"])
                logger.info("请求方式：%s" % caseinfo["request"]["method"])
                logger.info("请求路径：%s" % caseinfo["request"]["url"])
                # 判断请求头
                if set(request_keys).issuperset({"headers"}):
                    logger.info("请求头：%s" % caseinfo["request"]["headers"])

                # 加入公共参数
                if set(request_keys).issuperset({"params"}):
                    params = caseinfo["request"]["params"]
                    # update默认返回是none
                    params.update(load_ini())
                    caseinfo["request"]["params"] = params
                else:
                    params = {}
                    params.update(load_ini())
                    caseinfo["request"]["params"] = params

                # 通过对files进行处理，可以是所有文件
                for key, value in caseinfo['request'].items():
                    # print(key, value)
                    if key == "params":
                        logger.info("请求params参数：%s" % caseinfo["request"]["params"])
                    elif key == "data":
                        logger.info("请求data参数：%s" % caseinfo["request"]["data"])
                    elif key == "json":
                        logger.info("请求json参数：%s" % caseinfo["request"]["json"])
                    elif key == 'files':
                        logger.info("请求files参数：%s" % caseinfo["request"]["files"])

                        # print(key, value)
                        for file_key, file_value in value.items():
                            # print(file_key, file_value)
                            # 打开文件赋值给key[file_key]，用例中传输files时不用再进行处理
                            value[file_key] = open(file_value, "rb")

                # 发送请求,对caseinfo要解包
                res = self.send_all_request(**caseinfo['request'])
                # print(res.json())
                # print(res.text)
                logger.info("预期结果：%s" % caseinfo["validate"])
                logger.info("实际结果：%s" % res.text)

                # 提取中间变量
                self.extract_yaml_value(caseinfo, res)
                # return res
                # 断言封装
                # print(caseinfo['validate'])
                if caseinfo['validate']:  # 预期结果不为空
                    assert_result(caseinfo['validate'], res)
                # 接口测试通过
                logger.info("接口测试通过")
                logger.info("----------测试用例请求结束----------\n")

            else:
                print('yaml中的request目录中必须包含method，url')
                logger.info("----------测试用例请求结束----------\n")
        else:
            print('yaml一级目录必须包含feature,story，title，request，validate')
            logger.info("----------测试用例请求结束----------\n")

    # 封装的统一发送请求的方法
    # 使用**kwargs可变长度参数极限封装，因为传入的方法、参数等都是键值对，传入可变长度字典
    def send_all_request(self, **kwargs):
        # print(kwargs)  # 是一个字典
        # for key, value in kwargs.items():
        #     # print(key, value)
        #     if key == 'files':
        #         print(key, value)
        #         for file_key, file_value in value.items():
        #             print(file_key, file_value)
        #             # 打开文件赋值给key[file_key]，用例中传输files时不用再进行处理
        #             value[file_key] = open(file_value, 'rb')

        # 统一请求
        res = RequestUtil.sess.request(**kwargs)
        res1 = res.text.replace("\\/", "/")
        # print(res1)
        return res

    # 通过extract提取中间变量保存到extrac.yaml里
    def extract_yaml_value(self, caseinfo, res):
        if 'extract' in caseinfo.keys():
            for key, value in caseinfo['extract'].items():
                # 正则提取
                if "(.*?)" in value or "(.+?)" in value:
                    zz_value = re.findall(value, res.text)  # 提取多个值
                    # print(zz_value)
                    if len(zz_value) == 1:
                        # 只提取到一个值
                        data = {key: zz_value[0]}
                        write_yaml(data)
                    elif len(zz_value) == 0:
                        print("正则没有提取到任何值")
                    else:
                        # 提取到多个值
                        data = {key: zz_value}
                        write_yaml(data)
                else:  # jsonpath提取
                    json_value = jsonpath.jsonpath(res.json(), value)
                    if json_value:
                        if len(json_value) == 1:
                            # 只提取到一个值
                            data = {key: json_value[0]}
                            write_yaml(data)
                        elif len(json_value) == 0:
                            print("jsonpath没有提取到任何值")
                        else:
                            # 提取到多个值
                            data = {key: json_value}
                            write_yaml(data)

    # 热加载，httprunner
    def replace_hotload(self, yaml_str):
        regexp = "\\${(.*?)\\((.*?)\\)}"  # 正则替换匹配"${read_yaml(token1)}"
        # print(yaml_str)
        # 正则提取只针对字符串，因此返回值也为字符串
        fun_list = re.findall(regexp, yaml_str)
        # print(fun_list)
        for f in fun_list:
            # print(f'f[0]:{f[0]},f[1]:{f[1]}')
            # 多个参数打印 f[0]:read_yaml2,f[1]:csrf_token,0  f[1]返回为一个字符串，当成一个参数
            if f[1] != "":  # 不为空有参数
                # 使用反射调用
                # f[1]返回为一个字符串时，要用逗号切片成一个列表，并用*解包传参
                new_value = getattr(DebugTalk(), f[0])(*f[1].split(","))  # f[0]是函数名，f[1]是参数
                # print(f'f[0]:{f[0]},f[1]:{f[1].split(",")}')
            else:  # 没有参数
                print('没有参数')
                new_value = getattr(DebugTalk(), f[0])()
            # print(new_value)
            oldstr = "${" + f[0] + "(" + f[1] + ")}"  # 拼接旧值
            # print(oldstr)
            yaml_str = yaml_str.replace(oldstr, str(new_value))  # 用新值替换旧值，返回yaml_str
        return yaml_str
