# import re
# from pathlib import Path
#
# import allure
# import jsonpath as jsonpath
# import pytest
# import requests
#
# from commons.read_testcase_yaml_util import read_testcase
# from commons.request_util import RequestUtil
# from commons.yaml_util import read_yaml, write_yaml
#
# # 导入TestRegister模块会让原模块中的用例多执行一次，所以建立一个extract.yaml文件保存所有的中间变量
# # from testcases.b2c_testcases.test_login_api_wechat import TestRegister
#
# current_path = str(Path(__file__).parent)
#
#
# class TestPhp:
#
#     # 访问phpwind首页接口
#     # parametrize数据驱动，将yaml文件读取的列表字典嵌套[{}]格式的caseinfo，分解成字典格式{}
#     # caseinfo列表中有多个字典，parametrize数据驱动同样会分解成多个字典
#     @pytest.mark.parametrize('caseinfo', read_testcase(current_path + "./test_php1.yaml"))
#     def test_phpwind_start(self, caseinfo, base_url):
#         # print(caseinfo)   #一个字典
#         RequestUtil().standard_yaml(caseinfo, '')
#
#         # method = caseinfo['request']['method']
#         # url = caseinfo['request']['url']
#         # # url = 'http://47.107.116.139/phpwind/'
#         # # 保存返回结果
#         # # res = requests.get(url)
#         # res = RequestUtil().send_all_request(method=method, url=url)
#         # # 返回结果为html，保存在text中
#         # result = res.text
#         # # print(result)
#         # # 正则提取token
#         # # TestRegister.csrf_token = re.search('name="csrf_token" value="(.*?)"', result)[1]
#         # # 结果保存到中间文件extract.yaml中
#         # data = {"csrf_token": re.search('name="csrf_token" value="(.*?)"', result)[1]}
#         # write_yaml(data)
#
#     # 登录phpwind
#     @pytest.mark.parametrize('caseinfo', read_testcase(current_path + './test_php2.yaml'))
#     def test_login_phpwind(self, caseinfo, base_url):
#         RequestUtil().standard_yaml(caseinfo, '')
#
#         # method = caseinfo['request']['method']
#         # url = caseinfo['request']['url']
#         # headers = caseinfo['request']['headers']
#         # data = caseinfo['request']['data']
#         # data['csrf_token'] = read_yaml('csrf_token')
#         # # url = 'http://47.107.116.139/phpwind/index.php?m=u&c=login&a=dorun'
#         # # headers = {
#         # #     'Accept': 'application/json,text/javascript,/;q=0.01',
#         # #     'X-Requested-With': 'XMLHttpRequest'
#         # # }
#         # # data = {
#         # #     'username': 'baili',
#         # #     'password': 'baili123',
#         # #     # 'csrf_token': TestRegister.csrf_token,
#         # #     # 从中间文件extract.yaml中读取需要的参数
#         # #     'csrf_token': read_yaml("csrf_token"),
#         # #     'backurl': 'http://47.107.116.139/phpwind/',
#         # #     'invite': ''
#         # # }
#         # res = RequestUtil().send_all_request(method=method, url=url, data=data, headers=headers)
#         # # print(res.json())  # 返回失败，需要使用cookie关联
