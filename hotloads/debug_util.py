# -*- encoding：utf-8 -*-
# @Author: Kurosaki
# @Date Time: 2022/9/13 21:35
# @Filename: debug_util
# @Description:
import os

import yaml


class DebugTalk:

    # 读取yaml的数值，有一个参数
    def read_yaml(self, key):
        # os.getcwd()函数获得当前的路径，当前目录并不是指脚本所在的目录，而是所运行脚本的目录。
        with open(os.getcwd() + '/extract.yaml', encoding='utf-8', mode='r') as f:
            # value1 = yaml.load(f, yaml.FullLoader)
            # 读取文件第二种方法,安全加载
            value1 = yaml.safe_load(f)
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
    def read_yaml2(self, key, index):
        # os.getcwd()函数获得当前的路径，当前目录并不是指脚本所在的目录，而是所运行脚本的目录。
        with open(os.getcwd() + '/extract.yaml', encoding='utf-8', mode='r') as f:
            # value1 = yaml.load(f, yaml.FullLoader)
            # 读取文件第二种方法,安全加载
            value1 = yaml.safe_load(f)
            # index必须是一个整型，要强转成整型
            return value1[key][int(index)]
