# import allure
# import pytest
# import requests
#
# from commons.yaml_util import read_yaml
#
#
# class TestParametrize:
#     # @pytest.mark.parametrize("caseinfo", [{"name1": "大黑"}, {"name2": "小白"}])  # 读取数据实现数据驱动,传入数据最外层是字典列表
#     @pytest.mark.parametrize("caseinfo", read_yaml("./testcases/test1.yaml"))  # 可以直接传入读取数据方法
#     def test_userlogin(self, base_url, caseinfo):
#         # print(f'aaa{caseinfo}')
#         print('*' * 20)
#         print(caseinfo["story"])
#         print(caseinfo["title"])
#         print(caseinfo["request"]["method"])
#         print(base_url + caseinfo["request"]["url"])
#         print(caseinfo["request"]["headers"])
#         print(caseinfo["request"]["params"])
#         print(caseinfo["request"]["data"])
#         print(caseinfo["validate"])
#         print('*' * 20)
#
#         # 获取到yaml里面的参数
#         url = base_url + caseinfo["request"]["url"]
#         params = caseinfo["request"]["params"]
#         data = caseinfo["request"]["data"]
#
#         # 用post请求,返回一个结果
#         res = requests.post(url, json=data, params=params)
#         print(res.text)
