# # -*- encoding：utf-8 -*-
# # @Author: Kurosaki
# # @Date Time: 2022/9/16 22:27
# # @Filename: test_gzh
# # @Description:
# from pathlib import Path
#
# import pytest
#
# from commons.read_testcase_yaml_util import read_testcase
# from commons.request_util import RequestUtil
#
#
# # 调用该文件夹所属路径的上一级目录就相当于调用第一级父目录
# current_path = str(Path(__file__).parent)
#
#
# class TestGzh:
#     # 微信公众号获得access_token接口，get请求
#     @pytest.mark.run(order=1)
#     @pytest.mark.parametrize('caseinfo', read_testcase(current_path + '/test_gzh1.yaml'))
#     def test_get_access_token(self, caseinfo, base_url):
#         RequestUtil().standard_yaml(caseinfo, '')
#
#         # method = caseinfo['request']['method']
#         # url = caseinfo['request']['url']
#         # params = caseinfo['request']['params']
#         # # url = 'https://api.weixin.qq.com/cgi-bin/token'
#         # # param = {
#         # #     'grant_type': 'client_credential',
#         # #     'appid': 'wx8a9de038e93f77ab',
#         # #     'secret': '8326fc915928dee3165720c910effb86'
#         # # }
#         #
#         # # 保存返回结果
#         # res = RequestUtil().send_all_request(method=method, url=url, params=params)
#         # result = res.json()
#         # # print(result["access_token"])
#         # # TestRegister.access_token = result["access_token"]
#         # # print(TestRegister.access_token)
#         # # 结果保存到中间文件extract.yaml中
#         # data = {"access_token": result["access_token"]}
#         # # print(data)
#         # write_yaml(data)
#
#     # 微信公众号文件上传接口
#     @pytest.mark.parametrize('caseinfo', read_testcase(current_path + './test_gzh2.yaml'))
#     def test_fileupload(self, caseinfo, base_url):
#         RequestUtil().standard_yaml(caseinfo, '')
#
#         # method = caseinfo['request']['method']
#         # url = caseinfo['request']['url']
#         # # data = caseinfo['request']['data']
#         # # 通过files对文件进行处理，传到request_util进行处理
#         # files = caseinfo['request']['files']
#         # # data["media"] = open(data['media'], 'rb')
#         #
#         # params = {}
#         # params['access_token'] = read_yaml("access_token")
#         # # print(read_yaml("access_token"))
#         # # url = 'https://api.weixin.qq.com/cgi-bin/media/uploadimg'
#         # # param = {
#         # #     # 'access_token': TestRegister.access_token
#         # #     'access_token': read_yaml("access_token")
#         # # }
#         # # data = {
#         # #     # 文件上传要用open（）打开文件
#         # #     'media': open(r'C:\Users\kuros\Desktop\ResReader.png', 'rb')
#         # # }
#         # # 保存返回结果
#         # res = RequestUtil().send_all_request(method=method, url=url, files=files, params=params)
#         #
#         # result = res.json()
#         # print(result)
