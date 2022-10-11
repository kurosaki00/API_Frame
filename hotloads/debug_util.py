# -*- encoding：utf-8 -*-
# @Author: Kurosaki
# @Date Time: 2022/9/13 21:35
# @Filename: debug_util
# @Description:
import base64
import hashlib
import logging
import os
import random
import time
from io import StringIO
import re

import rsa
import yaml

logger = logging.getLogger(__name__)


class DebugTalk:
    # 读取config.yaml文件数据
    def read_config_yaml(self, key):
        with open(os.getcwd() + '/config.yaml', encoding='utf-8', mode='r') as f:
            # value1 = yaml.load(f, yaml.FullLoader)
            # 读取文件第二种方法,安全加载
            value = yaml.safe_load(f)
            return value[key]

    # 读取yaml的数值，有一个参数
    def read_yaml(self, key):
        # os.getcwd()函数获得当前的路径，当前目录并不是指脚本所在的目录，而是所运行脚本的目录。
        with open(os.getcwd() + '/extract.yaml', encoding='utf-8', mode='r') as f:
            # value1 = yaml.load(f, yaml.FullLoader)
            # 读取文件第二种方法,安全加载
            value1 = yaml.safe_load(f)
            # print(value1[key])
            return value1[key]

    # # 有一个参数和没有参数的方法可以合并用一个参数的方法
    # # 没有参数读取方法
    # def read_yaml1(self):
    #     # os.getcwd()函数获得当前的路径，当前目录并不是指脚本所在的目录，而是所运行脚本的目录。
    #     with open(os.getcwd() + '/extract.yaml', encoding='utf-8', mode='r') as f:
    #         # value1 = yaml.load(f, yaml.FullLoader)
    #         # 读取文件第二种方法,安全加载
    #         value1 = yaml.safe_load(f)
    #         return value1["access_token"]

    # 有两个参数的时候读取方法
    def read_yaml_of_index(self, key, index):
        # os.getcwd()函数获得当前的路径，当前目录并不是指脚本所在的目录，而是所运行脚本的目录。
        with open(os.getcwd() + '/extract.yaml', encoding='utf-8', mode='r') as f:
            # value1 = yaml.load(f, yaml.FullLoader)
            # 读取文件第二种方法,安全加载
            value1 = yaml.safe_load(f)
            # index必须是一个整型，要强转成整型
            return value1[key][int(index)]

    # 随机数时间戳,一般最长10位
    def get_time(self, length):
        return str(int(time.time()))[:length]

    # MD5加密
    def md5_encode(self, args):
        # 把变量转换成utf-8的格式,先转换成字符串，只有字符串才有encode
        args = str(args).encode("utf-8")
        # print(args)
        # MD5加密
        md5_value = hashlib.md5(args).hexdigest()
        # print(md5_value)
        return md5_value

    # base64加密
    def base64_encode(self, args):
        # 把变量转换成utf-8的格式,先转换成字符串，只有字符串才有encode
        args = str(args).encode("utf-8")
        # base64加密
        base64_value = base64.b64encode(args).decode(encoding="utf-8")
        return base64_value

    # # 生成RSA公钥和私钥（测试一般直接找开发拿到公钥私钥）
    # def create_rsa_key(self):
    #     # 生成密钥长度
    #     (public_key, private_key) = rsa.newkeys(1024)
    #     with open("./public.pem", "w+") as f:
    #         f.write(public_key.save_pkcs1().decode())
    #     with open("./private.pem", "w+") as f:
    #         f.write(private_key.save_pkcs1().decode())

    # RSA加密
    def rsa_encode(self, args):
        with open("./hotloads/public.pem", "r+", encoding="utf-8") as f:
            pubkey = rsa.PublicKey.load_pkcs1(f.read().encode())
        # 把变量转换成utf-8的格式,先转换成字符串，只有字符串才有encode
        args = str(args).encode("utf-8")
        # 把字符串加密成byte字节类型
        byte_value = rsa.encrypt(args, pubkey)
        # 把字节转换成字符串格式
        rsa_value = base64.b64encode(byte_value).decode("utf-8")
        return rsa_value

    # sign签名
    # def signs(self, yaml_path):
    #     all_dict_data = {}
    #     # 第一步
    #     with open(os.getcwd() + yaml_path, encoding="utf-8") as f:
    #         yaml_value = yaml.safe_load(f)
    #         print(yaml_value)
    #         for case in yaml_value:
    #             case_keys = case.keys()
    #             if "request" in case_keys:
    #                 request_value = case["request"]
    #                 if "url" in request_value:
    #                     # 把url的？后的值转化成字典
    #                     url = request_value["url"]
    #                     # 用切片取url中？后的参数键值
    #                     url = url[url.index("?") + 1:]
    #                     # print(url)
    #                     # 将url中取出的键值对切片成一个字符串列表
    #                     url_list = url.split("&")
    #                     # print(url_list)   #['m=u', 'c=login', 'a=dorun']
    #
    #                     for u in url_list:
    #                         # [u[0:u.index("=")]]为key，u[u.index("=") + 1:]为value
    #                         all_dict_data[u[0:u.index("=")]] = u[u.index("=") + 1:]
    #                     # print(all_dict_data)
    #                     # 得到params和data的参数
    #                     for key, value in request_value.items():
    #                         if key in ["data", "params"]:
    #                             for k, v in value.items():
    #                                 # print(k, v)
    #                                 # 写入{'csrf_token': 'mashang', 'appid': 'admin', 'appsecret': '123'}
    #                                 all_dict_data[k] = v
    #                     # 把字典的key按照ASCII码升序排列
    #                     all_dict_data = self.dict_ascii_sort(all_dict_data)
    #                     # print(all_dict_data)
    #                     # 如果值是变量，需要用热加载处理
    #                     yaml_str = yaml.dump(all_dict_data)  # 把字典转换成字符串,建议使用
    #                     # yaml_str = json.dumps(caseinfo)  # 把字典转换成字符串
    #                     yaml_str = self.replace_hotload(yaml_str)
    #                     all_dict_data = yaml.safe_load(StringIO(yaml_str))  # 字符转换成字符串文件流再转成字典，提取的是整型就是整型，字符串就是字符串
    #                     print(all_dict_data)
    #
    #     # 第二步，字典转换成字符串&连接
    #     all_str = ""
    #     for key, value in all_dict_data.items():
    #         all_str = all_str + str(key) + "=" + str(value) + "&"
    #     all_str = all_str[:-1]
    #
    #     # 第三-五步
    #     appid = "admin"
    #     appsecret = "123"
    #     nonce = str(random.randint(1000000000, 9999999999))
    #     timestamp = str(int(time.time()))
    #     all_str = "appid=" + appid + "&appsecret=" + appsecret + "&" + all_str
    #           + "&nonce=" + nonce + "&timestamp=" + timestamp
    #     # print(all_str)
    #     # 第六步
    #     sign = self.md5_encode(all_str).upper()
    #     print(sign)
    #     return sign

    # 带数据驱动的签名
    def ddt_sign(self, yaml_path, index):
        all_dict_data = {}
        # 第一步
        with open(os.getcwd() + yaml_path, encoding="utf-8") as f:
            yaml_value = yaml.safe_load(f)  # 列表
            # print(yaml_value)

            # 加入数据驱动
            new_caseinfo = self.ddts(*yaml_value)
            case = new_caseinfo[int(index)]

            # 处理签名
            case_keys = case.keys()
            if "request" in case_keys:
                request_value = case["request"]
                if "url" in request_value:
                    url = request_value["url"]
                    # 用切片取url中？后的参数键值
                    url = url[url.index("?") + 1:]
                    # 将url中取出的键值对切片成一个字符串列表
                    url_list = url.split("&")
                    # print(url_list)   #['m=u', 'c=login', 'a=dorun']

                    for u in url_list:
                        # [u[0:u.index("=")]]为key，u[u.index("=") + 1:]为value
                        all_dict_data[u[0:u.index("=")]] = u[u.index("=") + 1:]
                    # 得到params和data的参数
                    for key, value in request_value.items():
                        if key in ["data", "params"]:
                            for k, v in value.items():
                                # print(k, v)
                                # 写入{'csrf_token': 'mashang', 'appid': 'admin', 'appsecret': '123'}
                                all_dict_data[k] = v
                    # 把字典的key按照ASCII码升序排列
                    all_dict_data = self.dict_ascii_sort(all_dict_data)
                    # print(all_dict_data)
                    # 如果值是变量，需要用热加载处理
                    yaml_str = yaml.dump(all_dict_data)  # 把字典转换成字符串,建议使用
                    # yaml_str = json.dumps(caseinfo)  # 把字典转换成字符串
                    yaml_str = self.replace_hotload(yaml_str)
                    all_dict_data = yaml.safe_load(StringIO(yaml_str))  # 字符转换成字符串文件流再转成字典，提取的是整型就是整型，字符串就是字符串
                    # print(all_dict_data)

        # 第二步，字典转换成字符串&连接
        all_str = ""
        for key, value in all_dict_data.items():
            all_str = all_str + str(key) + "=" + str(value) + "&"
        all_str = all_str[:-1]
        # print(all_str)
        sign = self.md5_encode(all_str).upper()
        # print(sign)
        return sign

    #流程用例的sign签名
    def flow_sign(self, yaml_path, index):
        all_dict_data = {}
        # 第一步
        with open(os.getcwd() + yaml_path, encoding="utf-8") as f:
            yaml_value = yaml.safe_load(f)  # 列表
            # print(yaml_value)

            # 不需要数据驱动
            # new_caseinfo = self.ddts(*yaml_value)
            case = yaml_value[int(index)]

            # 处理签名
            case_keys = case.keys()
            if "request" in case_keys:
                request_value = case["request"]
                if "url" in request_value:
                    url = request_value["url"]
                    # 用切片取url中？后的参数键值
                    url = url[url.index("?") + 1:]
                    # 将url中取出的键值对切片成一个字符串列表
                    url_list = url.split("&")
                    # print(url_list)   #['m=u', 'c=login', 'a=dorun']

                    for u in url_list:
                        # [u[0:u.index("=")]]为key，u[u.index("=") + 1:]为value
                        all_dict_data[u[0:u.index("=")]] = u[u.index("=") + 1:]
                    # 得到params和data的参数
                    for key, value in request_value.items():
                        if key in ["data", "params"]:
                            for k, v in value.items():
                                # print(k, v)
                                # 写入{'csrf_token': 'mashang', 'appid': 'admin', 'appsecret': '123'}
                                all_dict_data[k] = v
                    # 把字典的key按照ASCII码升序排列
                    all_dict_data = self.dict_ascii_sort(all_dict_data)
                    # print(all_dict_data)
                    # 如果值是变量，需要用热加载处理
                    yaml_str = yaml.dump(all_dict_data)  # 把字典转换成字符串,建议使用
                    # yaml_str = json.dumps(caseinfo)  # 把字典转换成字符串
                    yaml_str = self.replace_hotload(yaml_str)
                    all_dict_data = yaml.safe_load(StringIO(yaml_str))  # 字符转换成字符串文件流再转成字典，提取的是整型就是整型，字符串就是字符串
                    # print(all_dict_data)

        # 第二步，字典转换成字符串&连接
        all_str = ""
        for key, value in all_dict_data.items():
            all_str = all_str + str(key) + "=" + str(value) + "&"
        all_str = all_str[:-1]
        # print(all_str)
        sign = self.md5_encode(all_str).upper()
        # print(sign)
        return sign

    # 把字典的key按照ASCII码升序排列
    def dict_ascii_sort(self, args_dict):
        dict_key = dict(args_dict).keys()
        l = list(dict_key)
        l.sort()
        new_dict = {}
        for key in l:
            new_dict[key] = args_dict[key]
        return new_dict

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

    # 解析parametrize数据驱动
    def ddts(self, caseinfo):
        # yaml_util文件中要获取替换值，caseinfo必须是字符串的格式，将字典转换成字符串
        # str_caseinfo = json.dumps(caseinfo)#用json转换,需要注意数据类型的转换
        str_caseinfo = yaml.dump(caseinfo)  # 用yaml转换为字符串,不需要关注数据类型
        # print(caseinfo)  # 字典
        # print(str_caseinfo)  # 字符串
        # 获取parametrize的数据
        caselist = caseinfo["parametrize"]
        # 初步判断长度是否异常
        length_flag = True
        # 获取parametrize中第一行第一个列表（即参数名列表）的长度
        name_length = len(caselist[0])
        for p in caselist:
            # 判断之后的数据列表中的长度是否和参数名列表长度相同
            if len(p) != name_length:
                length_flag = False
                # print(f"{p}数据长度有误")
                logger.info(f"{p}数据长度有误")
        # 长度没问题
        new_caseinfo = []
        if length_flag:
            # 判断parametrize行数,i表示行数,从第二行开始循环
            for i in range(1, len(caselist)):
                # 将yaml文件中的数据字符串作为每一行单独的数据，开始循环
                raw_caseinfo = str_caseinfo
                for j in range(name_length):  # j表示列
                    # print(caselist[i][j])
                    if isinstance(caselist[i][j], str):
                        caselist[i][j] = "'" + str(caselist[i][j]) + "'"  # 解决数字字符串变成数字类型的问题
                        # print(caselist[i][j])
                    raw_caseinfo = raw_caseinfo.replace("$ddt{" + caselist[0][j] + "}", str(caselist[i][j]))

                # 用yaml进行格式转换，不用考虑数据类型问题
                new_caseinfo.append(yaml.safe_load(StringIO(raw_caseinfo)))  # 字符串文件流再转成字典，提取的是整型就是整型，字符串就是字符串
        # 返回替换后的结果列表字典
        # print(new_caseinfo)
        return new_caseinfo


if __name__ == '__main__':
    # print(DebugTalk().create_rsa_key())
    pass
