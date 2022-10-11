# import re
#
# import allure
# import jsonpath as jsonpath
# import pytest
# import requests
#
# from commons.yaml_util import read_yaml
#
#
# @allure.epic("项目名称：电商接口自动化测试")  # 常用
# @allure.feature("模块名称：用户管理模块用例")  # 常用
# # class TestRegister:
# #     """
# #         def test_regis(self, base_url):
# #             requests.get()
# #             requests.post()
# #             requests.put()
# #             requests.delete()
# #             requests.request()
# #             s = requests.session()  # 返回session的对象,也有一个request（）方法
# #             s.request()
# #
# #         def get(url, params=None, **kwargs):  # 发送get请求
# #             # url接口请求地址
# #             # params是ger请求用于传参的，会自动以？的方式加到url之后，多个参数之间用&分割
# #             # **kwargs:可变长度字典参数
# #             pass
# #
# #         def post(url, data, json, **kwargs):  # 发送post请求
# #             # data：用于传参，接口文档中的表格
# #             # json：用于传参，接口文档中的json格式，工具中用raw-json传参
# #             # files:用于文件上传
# #
# #             # 基于postman
# #             # form-data:既有表单参数（data传参），也有文件上传（files传参）
# #             # x-www-form-urlencoded：100%表单（data传参）
# #             # raw：json（json传参），xml（data传参），text（data传参）
# #             # binary：二进制文件上传（data传参）
# #             pass
# #
# #         def put(url, data, **kwargs):  # 发送put请求
# #             pass
# #
# #         def delete(url, **kwargs):  # 发送delete请求
# #             pass
# #
# #         # --------------------------------------------------
# #         def request(method, url, **kwargs):  # 发送任意请求，以上四种任意一个，是get、post、put、delete的底层方法
# #             # get、post、put、delete调用request方法，request又调用session.request方法
# #             pass
# #
# #         # ------------------------------------------------------
# #         # requests.request()和session.request()两者区别在于：
# #         # 前者的每个请求都是独立的，而后者会自动的关联所有请求的cookie信息（类似于jmeter的http cookie管理器的作用）
# #         def session():  # 获得一个session对象
# #             def request(  # session对象的request方法
# #                     self,
# #                     method,  # 请求方式
# #                     url,  # 请求路径
# #                     params=None,  # 请求参数
# #                     data=None,  # data参数
# #                     json=None,  # json参数
# #                     headers=None,  # 请求头
# #                     cookies=None,  # cookiexinxi
# #                     files=None,  # 文件上传
# #                     # ----------------------------#上面重要，底下不常用
# #                     auth=None,  # 鉴权
# #                     timeout=None,  # 超市处理
# #                     allow_redirects=True,  # 重定向
# #                     proxies=None,  # 代理
# #                     hooks=None,  # 钩子函数
# #                     stream=None,  # 文件下载
# #                     verify=None,  # CA证书验证
# #                     cert=None
# #             ):
# #                 pass
# #
# #         响应内容：
# #         res.test:把返回结果转化成文本输出
# #         res.json（）:把返回结果转化成字典输出
# #         res.content:把返回转换成字节输出
# #         res.status_code:返回状态码
# #         res.reason:返回状态信息
# #         res.cookie：cookie信息
# #         res.encoding:编码格式
# #         res.headers:响应头
# #         --------------------------------------------
# #         res.request.xxxxxx:返回请求的信息
# #     """
# #
# #     def test_regis(self):
# #         url = 'http://101.34.221.219:8010/api.php?s=user/login'
# #         param = {
# #             'application': 'app',
# #             'application_client-type': 'h5'
# #         }
# #         json = {
# #             "accounts": "baili",
# #             "pwd": "baili123",
# #             "type": "username"
# #         }
# #         # 保存返回结果
# #         res = requests.post(url, json=json, params=param)
# #         print(res.json())
# #         print(res.text)
# #
# #         # 正则表达式提取token,两种方法，正则应对的是字符串
# #         # 两者的区别，第一个通过下标取值，只匹配到一个值；第二个匹配多个值，返回列表，多个值通过下标取值，没匹配到返回none
# #         # 第一种：re.search(‘正则’，res.text),通过下标为[1]取值,没匹配到返回none
# #         token = re.search('"token":"(.*?)",', res.text)[1]
# #         print(f'token1：{token}')
# #         # 第二种：re.findall(‘正则’，res.text)
# #         token = re.findall('"token":"(.*?)"', res.text)
# #         print(f'token2：{token}')
# #
# #         # jsonpath提取token，返回的是一个列表，通过下标取值，没找到返回none，类似re.findall()
# #         # jsonpath.jsonpath(对象res.json()，jsonpath表达式)
# #         # '$.data.token':$表示根，根下的data-->token
# #         token = jsonpath.jsonpath(res.json(), '$.data.token')
# #         print(f'token3：{token}')
# #
# #         # 不通过以上两种方式取token
# #         result = res.json()
# #         token = result["data"]["token"]
# #         print(f'token4：{token}')
#
# # 接口关联两种方法
# # 1、类变量
# class TestRegister:
#     # 定义一个空的类变量
#     token = ''
#     access_token = ''
#     csrf_token = ''
#     cookies = ''
#     # 定义一个session，用来关联cookies
#     sess = requests.session()
#
#     def test_regis(self):
#         url = 'http://101.34.221.219:8010/api.php?s=user/login'
#         param = {
#             'application': 'app',
#             'application_client-type': 'h5'
#         }
#         json = {
#             "accounts": "baili",
#             "pwd": "baili123",
#             "type": "username"
#         }
#
#         # 保存返回结果
#         # res = requests.post(url, json=json, params=param)
#         # 关联session后，不再用requests方法，用session的方法,使用参数method，所有用例会自动关联cookies
#         res = TestRegister.sess.request(method='post', url=url, json=json, params=param)
#         result = res.json()
#         # 结果保存到类变量
#         TestRegister.token = result["data"]["token"]
#         print(f'token：{TestRegister.token}')
#
#     # 订单列表接口
#     def test_order(self):
#         url = 'http://101.34.221.219:8010/api.php?s=order/index'
#         param = {
#             'application': 'app',
#             'application_client-type': 'h5',
#             # 传入上一个用例获取到的token
#             'token': TestRegister.token
#         }
#         json = {
#             "page": 1,
#             "keywords": "",
#             "status": "-1",
#             "is_more": 1
#         }
#         # 保存返回结果
#         # res = requests.post(url, json=json, params=param)
#         res = TestRegister.sess.request(method='post', url=url, json=json, params=param)
#
#         result = res.json()
#         print(result)
#
#     # 微信公众号获得access_token接口，get请求
#     def test_wechat(self):
#         url = 'https://api.weixin.qq.com/cgi-bin/token'
#         param = {
#             'grant_type': 'client_credential',
#             'appid': 'wx8a9de038e93f77ab',
#             'secret': '8326fc915928dee3165720c910effb86'
#         }
#
#         # 保存返回结果
#         # res = requests.get(url, params=param)
#         res = TestRegister.sess.request(method='get', url=url, params=param)
#         result = res.json()
#         # print(result)
#         TestRegister.access_token = result["access_token"]
#         print(TestRegister.access_token)
#
#     # 微信公众号文件上传接口
#     def test_fileupload(self):
#         url = 'https://api.weixin.qq.com/cgi-bin/media/uploadimg'
#         param = {
#             'access_token': TestRegister.access_token
#         }
#         data = {
#             # 文件上传要用open（）打开文件
#             'media': open(r'C:\Users\kuros\Desktop\ResReader.png', 'rb')
#         }
#         # 保存返回结果
#         # res = requests.post(url, files=data, params=param)
#         res = TestRegister.sess.request(method='post', url=url, files=data, params=param)
#
#         result = res.json()
#         print(result)
#         # TestRegister.access_token = result["access_token"]
#         # print(TestRegister.access_token)
#
#     # 访问phpwind首页接口
#     def test_phpwind(self):
#         url = 'http://47.107.116.139/phpwind/'
#         # 保存返回结果
#         # res = requests.get(url)
#         res = TestRegister.sess.request(method='get', url=url)
#         # 返回结果为html，保存在text中
#         result = res.text
#         # print(result)
#         # 正则提取token
#         TestRegister.csrf_token = re.search('name="csrf_token" value="(.*?)"', result)[1]
#
#         # session.request关联cookies，不需要再获取和传输cooki
#         # TestRegister.cookies = res.cookies
#
#     # 登录phpwind
#     def test_phpwind_login(self):
#         url = 'http://47.107.116.139/phpwind/index.php?m=u&c=login&a=dorun'
#         headers = {
#             'Accept': 'application/json,text/javascript,/;q=0.01',
#             'X-Requested-With': 'XMLHttpRequest'
#         }
#         data = {
#             'username': 'baili',
#             'password': 'baili123',
#             'csrf_token': TestRegister.csrf_token,
#             'backurl': 'http://47.107.116.139/phpwind/',
#             'invite': ''
#         }
#
#         # res = requests.post(url,data=data,headers=headers,cookies=TestRegister.cookies)
#         # cookies=TestRegister.cookies不需要再传参
#         res = TestRegister.sess.request(method='post', url=url, data=data, headers=headers)
#         result = res.json()
#         print(result)  # 返回失败，需要使用cookie关联
#
#         # 失败时可以去掉headers，通过返回的headers查看错误信息
#         # res = requests.post(url, data=data, cookies=TestRegister.cookies)
#         # result = res.text  # 此时要打印文本
#         # print(result)  # 查看提示信息，此处没有提示
#
# # 2、单独文件保存
