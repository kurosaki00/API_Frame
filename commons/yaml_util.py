import os

import yaml


# # 读取yaml的数值
# def read_yaml(yaml_path):
#     with open(yaml_path, encoding='utf-8', mode='r') as f:
#         # value1 = yaml.load(f, yaml.FullLoader)
#         # 读取文件第二种方法,安全加载
#         value1 = yaml.safe_load(f)
#         return value1
#
#
# # 写入yaml的数值
# def write_yaml(yaml_path):
#     # mode为w表示清空原内容写入，a表示在原内容的基础上增加
#     with open(yaml_path, encoding='utf-8', mode='a') as f:
#         data = {"name": "大白"}
#         yaml.dump(data, f, allow_unicode=True)  # 写入,允许使用Unicode编码，解决中文乱码
#
#
# # 清空
# def clear_yaml(yaml_path):
#     with open(yaml_path, encoding='utf-8', mode='w') as f:
#         f.truncate()  # 清空打开文件方式用w,清空方法用文件自带的方法truncate()
#
#
# if __name__ == '__main__':
#     value = read_yaml('../testcases/test1.yaml')
#     print(value)  # 键值对，打印结果是一个字典
#     # write_yaml('../testcases/testyaml.txt')
#     # print(value['data1'], type(value['data1']))
#     # print(value['data2'], type(value['data2']))
#     # print(value['data3'], type(value['data3']))
#     # print(value['data4'], type(value['data4']))
#     # print(value['data5'], type(value['data5']))
#     # print(value['data6'], type(value['data6']))
#     # print(value['data7'], type(value['data7']))
#     # print(value['data8'], type(value['data8']))
#     # print(value['data9'], type(value['data9']))
#     # print(value['data10'], type(value['data10']))
#     # print(value['data11'], type(value['data11']))
#     # print(value['data13'], type(value['data13']))

# 读取yaml的数值
def read_yaml(key):
    # os.getcwd()函数获得当前的路径，当前目录并不是指脚本所在的目录，而是所运行脚本的目录。
    with open(os.getcwd() + '/extract.yaml', encoding='utf-8', mode='r') as f:
        # value1 = yaml.load(f, yaml.FullLoader)
        # 读取文件第二种方法,安全加载
        value1 = yaml.safe_load(f)
        return value1[key]


# 写入yaml的数值
def write_yaml(data):
    # mode为w表示清空原内容写入，a表示在原内容的基础上增加
    with open(os.getcwd() + '/extract.yaml', encoding='utf-8', mode='a') as f:
        # data = {"name": "大白"}
        yaml.dump(data, f, allow_unicode=True)  # 写入,允许使用Unicode编码，解决中文乱码


# 清空
def clear_yaml():
    with open(os.getcwd() + '/extract.yaml', encoding='utf-8', mode='w') as f:
        f.truncate()  # 清空打开文件方式用w,清空方法用文件自带的方法truncate()


# # 读取测试用例的方法
# def read_testcase(yaml_path):
#     with open(yaml_path, encoding='utf-8', mode='r') as f:
#         value = yaml.load(f, yaml.FullLoader)
#         # print(value) # 读取到的返回值是一个列表，嵌套一个字典,[{}]
#         return value


# # 读取config.yaml文件数据
# def read_config_yaml(key):
#     with open(os.getcwd() + '/config.yaml', encoding='utf-8', mode='r') as f:
#         # value1 = yaml.load(f, yaml.FullLoader)
#         # 读取文件第二种方法,安全加载
#         value = yaml.safe_load(f)
#         return value[key]


if __name__ == '__main__':
    value = read_yaml()
    print(value)  # 键值对，打印结果是一个字典
    # write_yaml('../testcases/testyaml.txt')
    # print(value['data1'], type(value['data1']))
    # print(value['data2'], type(value['data2']))
    # print(value['data3'], type(value['data3']))
    # print(value['data4'], type(value['data4']))
    # print(value['data5'], type(value['data5']))
    # print(value['data6'], type(value['data6']))
    # print(value['data7'], type(value['data7']))
    # print(value['data8'], type(value['data8']))
    # print(value['data9'], type(value['data9']))
    # print(value['data10'], type(value['data10']))
    # print(value['data11'], type(value['data11']))
    # print(value['data13'], type(value['data13']))
