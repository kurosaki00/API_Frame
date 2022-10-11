# import re
# from pathlib import Path
#
# import allure
# import jsonpath as jsonpath
# import pytest
# import requests
#
# from commons.ddt_util import read_testcase
# from commons.request_util import RequestUtil
# from commons.yaml_util import read_yaml, write_yaml
#
# # 无论在哪里执行，都是获取当前文件的绝对路径，window路径，要强转成str
# current_path = str(Path(__file__).parent)
#
#
# class TestLogin:
#     # 定义一个空的类变量
#     # token = ''
#     # access_token = ''
#     # csrf_token = ''
#     # @pytest.mark.parametrize('caseinfo', read_testcase('./testcases/b2c_testcases/test_b2c1.yaml'))
#     @pytest.mark.parametrize('caseinfo', read_testcase(current_path + '/test_b2c1.yaml'))
#     def test_login_b2c(self, caseinfo, base_url):
#         # print(caseinfo)
#         # 判断yaml的数据格式是否符合框架的规范
#         RequestUtil().standard_yaml(caseinfo, base_url)
#         # print(res.json())
#         # # print(caseinfo)
#         # method = caseinfo['request']['method']
#         # url = base_url + caseinfo['request']['url']
#         # params = caseinfo['request']['params']
#         # data = caseinfo['request']['data']
#         # # print(url,method,params,data)
#         # #   url = 'http://101.34.221.219:8010/api.php?s=user/login'
#         # #     param = {
#         # #         'application': 'app',
#         # #         'application_client-type': 'h5'
#         # #     }
#         # #     json = {
#         # #         "accounts": "baili",
#         # #         "pwd": "baili123",
#         # #         "type": "username"
#         # #     }
#         # #
#         # #     # 保存返回结果
#         # res = RequestUtil().send_all_request(method=method, url=url, data=data, params=params)
#         # result = res.json()
#         # #     # # 结果保存到类变量
#         # #     # TestRegister.token = result["data"]["token"]
#         # #     # print(f'token：{TestRegister.token}')
#         # #     # 结果保存到中间文件extract.yaml中
#         # data = {"token": result["data"]["token"]}
#         # write_yaml(data)
#         # print(result)
#
#     # 订单列表接口
#     @pytest.mark.parametrize('caseinfo', read_testcase(current_path + '/test_b2c2.yaml'))
#     def test_order_list(self, caseinfo, base_url):
#         RequestUtil().standard_yaml(caseinfo, base_url)
#
#         # method = caseinfo['request']['method']
#         # url = base_url + caseinfo['request']['url']
#         # params = caseinfo['request']['params']
#         # params['token'] = read_yaml("token")
#         # data = caseinfo['request']['data']
#         # # url = 'http://101.34.221.219:8010/api.php?s=order/index'
#         # # param = {
#         # #     'application': 'app',
#         # #     'application_client-type': 'h5',
#         # #     # 传入上一个用例获取到的token
#         # #     # 'token': TestRegister.token
#         # #     'token': read_yaml("token")
#         # # }
#         # # json = {
#         # #     "page": 1,
#         # #     "keywords": "",
#         # #     "status": "-1",
#         # #     "is_more": 1
#         # # }
#         # # 保存返回结果
#         # # res = requests.post(url, json=json, params=param)
#         # res = RequestUtil().send_all_request(method=method, url=url, data=data, params=params)
#
#         # result = res.json()
#         # print(result)
#
#     # 订单详情接口
#     @pytest.mark.parametrize('caseinfo', read_testcase(current_path + '/test_b2c_orderdetail.yaml'))
#     def test_order_detail(self, caseinfo, base_url):
#         RequestUtil().standard_yaml(caseinfo, base_url)
