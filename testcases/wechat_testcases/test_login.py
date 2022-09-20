# import allure
# import pytest
# from commons.yaml_util import read_yaml
# # @pytest.mark.usefixtures("exe_sql")   # scope为class，手动调用时，指定类执行时需要在类前加装饰器
#
#
# """
# 一般企业中常用的allure方法：
# 1、@allure.epic("项目名称：电商接口自动化测试")
# 2、@allure.feature("模块名称：用户管理模块用例")
# 3、@allure.story("接口名称：登录接口")
# 4、@allure.title("用例名称：验证接口登录成功-正例")
# 5、@allure.description("用例描述：登录")
# 6、@allure.severity(allure.severity_level.CRITICAL)
#
# 不常用的：
# # 增加测试用例的步骤
# for i in range(1, 6):
#     with allure.step(f"第{i}步操作步骤如下:"):
#         print(f"执行第{i}步")
# # 增加测试用例的附件
# with open("C:\\Users\\kuros\\Desktop\\ResReader.png", mode="rb") as f:  # 以二进制形式读取文件
#     content = f.read()
#     # 附件内容content，附件名name，附件类型type
#     allure.attach(body=content, name="错误截图", attachment_type=allure.attachment_type.PNG)
# # 加文本
# allure.attach("{a:hhh}", "响应内容", allure.attachment_type.TEXT)
# """
#
#
# @allure.epic("项目名称：电商接口自动化测试")  # 常用
# @allure.feature("模块名称：用户管理模块用例")  # 常用
# class TestLogin:
#
#     # def setup_class(self):
#     #     print("类之前执行")
#     #
#     # def teardown_class(self):
#     #     print("类之后执行")
#     #
#     # def setup(self):
#     #     print("用例之前执行")
#     #
#     # def teardown(self):
#     #     print("用例之后执行")
#
#     # @pytest.mark.smoke
#     # def test_login_shopxo(self, sql):  # fixture固件参数化时需要传入固件名，固件名有别名的，要修改为别名
#     #     print("登录用例" + sql)
#     @allure.story("接口名称：登录接口")  # 常用
#     # 用例名称的第一种写法，方法上加装饰器，用title（）方法
#     @allure.title("用例名称：验证接口登录成功-正例")  # 常用
#     @allure.description("用例描述：登录")  # 常用
#     # 五种用例级别：BLOCK阻塞，CRITICAL严重，NORMAL一般，提升MINOR，轻微TRIVIAL
#     @allure.severity(allure.severity_level.CRITICAL)  # 常用
#     # 以下为不常用的三种方法
#     @allure.link("访问接口的链接")
#     @allure.issue("bug链接")
#     @allure.testcase("测试用例的链接")
#     def test_login_shopxo(self, base_url):  # fixture固件参数化时需要传入固件名
#         url = "user/login"
#         all_url = f"{base_url}{url}"
#         print(all_url)
#         print("登录用例")
#         # assert 'http' in all_url
#         # assert 1 == 2
#         # 增加测试用例的步骤
#         for i in range(1, 6):
#             with allure.step(f"第{i}步操作步骤如下:"):
#                 print(f"执行第{i}步")
#         # 增加测试用例的附件
#         with open("C:\\Users\\kuros\\Desktop\\ResReader.png", mode="rb") as f:  # 以二进制形式读取文件
#             content = f.read()
#             # 附件内容content，附件名name，附件类型type
#             allure.attach(body=content, name="错误截图", attachment_type=allure.attachment_type.PNG)
#         # 加文本
#         allure.attach("{a:hhh}", "响应内容", allure.attachment_type.TEXT)
#
#     # @pytest.mark.run(order=1)  # 按照设置的序号执行
#     @allure.story("接口名称：注册接口")
#     def test_register(self):
#         # 用例名称的第二种写法，方法内用allure.dynamic.title()方法
#         allure.dynamic.title("用例名称：验证接口注册成功-正例")
#         print("注册用例")
#
#     # @pytest.mark.product_manage
#     # @pytest.mark.skip(reason="跳过")  #跳过用例，无条件和有条件skipif，跳过理由可选
#     @allure.story("接口名称：查询订单接口")
#     @allure.title("用例名称：查询订单用例")
#     def test_select_orders(self):
#         print("查询订单")
#
#
#
#
# # 用例执行顺序
# # 用例执行顺序，默认按照文件夹名、py文件名、用例名的ASCII码的顺序依次执行，如a-z
# # 可以通过pytest-ordering插件改变默认的用例执行顺序
