# -*- encoding：utf-8 -*-
# @Author: Kurosaki
# @Date Time: 2022/9/18 14:33
# @Filename: read_testcase_yaml_util
# @Description: parametrize数据驱动
import json
import logging
from io import StringIO

import yaml

logger = logging.getLogger(__name__)


# 读取测试用例的方法,从yaml_util中独立出来，实现[{}]-->{}的parametrize数据驱动
def read_testcase(yaml_path):
    with open(yaml_path, encoding='utf-8', mode='r') as f:
        caseinfo = yaml.load(f, yaml.FullLoader)
        # print(caseinfo)  # 读取到的返回值是一个列表，嵌套一个字典,[{}]
        if len(caseinfo) >= 2:  # 通过复制yaml数据的方式实现数据驱动,即yaml文件里复制有多个用例数据
            # return caseinfo
            return [caseinfo]  #流程用例
        else:  # 通过parametrize实现数据驱动
            # 列表格式caseinfo解包成字典，字典中的所有key得到字典，判断parametrize是否在该keys字典中
            if "parametrize" in dict(*caseinfo).keys():
                # print("使用了parametrize数据驱动")
                new_caseinfo = ddts(*caseinfo)
                # print(new_caseinfo)
                return new_caseinfo
            else:
                # print("没用parametrize数据驱动")
                return caseinfo
        # return caseinfo


# 解析parametrize数据驱动
def ddts(caseinfo):
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

                # 通过json格式转换，要考虑数据类型转换

                # # 如果数据中有不是字符串的（整型、浮点型、列表等），必须先进行判断，进行数据处理
                # if not isinstance(caselist[i][j], str):
                #     # print('"$ddt{"'+ caselist[0][j] + '"}"', caselist[i][j])
                #     # 返回字符串中的"$ddt{pwd}"整体替换成123
                #     raw_caseinfo = raw_caseinfo.replace('"$ddt{' + caselist[0][j] + '}"',
                #                                         str(caselist[i][j]).replace('\'', '\"'))
                # else:
                #     # 将第一行的旧值$ddt{caselist[0][j]}，替换成新值caselist[i][j],新旧值必须都是字符串
                #     raw_caseinfo = raw_caseinfo.replace("$ddt{" + caselist[0][j] + "}", str(caselist[i][j]))
                # print(raw_caseinfo)
            # 每一行循环完之后，将结果转换为字典添加到新的列表中
            # new_caseinfo.append(json.loads(raw_caseinfo))  # 字符串转换为json格式，json只认双引号不认单引号

            # 用yaml进行格式转换，不用考虑数据类型问题
            new_caseinfo.append(yaml.safe_load(StringIO(raw_caseinfo)))  # 字符串文件流再转成字典，提取的是整型就是整型，字符串就是字符串
    # 返回替换后的结果列表字典
    # print(new_caseinfo)
    return new_caseinfo
