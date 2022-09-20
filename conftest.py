# conftest.py，文件名固定写法，专门用来存放附件的py文件
# 不需要做任何的导包，不管是在根目录，还是在用例目录，还是在模块目录，都会被自动发现加载并执行。
# 执行顺序，从最外面往最内层执行，从大文件夹到小文件夹执行。如果是同一个conftest那么按照固件名的ASCII码先后执行。

"""
夹具的优先级
1、先执行当前目录下（此处的项目目录下）的conftest.py里面的fixtrue的类级别
2、读取pytest.ini配置，找到测试用例
3、执行测试用例目录（此处的testcases目录下）下的congtest.py文件中的fixtrue的类级别
4、执行测试用例-->模块目录（此处的testcases下的子目录，如有）下的conftest.py文件中的fixtrue的类级别
5、setup_class
6、然后按当前目录、测试用例目录、测试用例下的模块目录的函数级别
7、setup
8、执行测试用例
9、然后从里到外一次执行后置
"""
import pytest

# 加上清空extract.yaml的固件，程序执行前会先清空原文件里的内容
from commons.yaml_util import clear_yaml


@pytest.fixture(scope="session", autouse=True)
def clear_extract():
    clear_yaml()

# fixture固件
# @pytest.fixture(scope='class', autouse=False, params=['haha', 'heihei'], ids=['a', 'b'], name='sql')
# @pytest.fixture(scope='class', autouse=True)
# def exe_sql(request):  # 参数化时需要传入request
#     print('执行sql')
# 参数化时yield后面需要加request.param
# yield request.param  # yield生成器作用基本和return类似，区别在于return后不执行，yield之后继续执行
# yield
# print('关闭数据库连接')

# pytest前后置（固件、夹具）
# 在用例之前和用例之后要进行的操作==前置操作和后置操作，如setup、teardown

# fixture固件
# fixture的语法：
# @pytest.fixtrue(scope="作用域", autouse="自动使用", params="参数化", ids="参数别名",name="固件别名")
# 1、scope
#   function函数级别生效，class级别生效，module模块级别（可理解为当前py文件）生效，package/session会话级别（可理解为当前python包文件）生效
#   score=class，手动调用时，指定类执行时需要在类前加装饰器@pytest.mark.usefixtures("exe_sql")，不指定对所有类生效
#   score=module的场景很少（一般只有自动，如果一个模块中只有一个类，那么module和class的效果差不多）
#   score=package/session的场景（一般只有自动，整个会话指指定文件夹中所有的文件、用例，从用例开始执行到结束的整个过程中的用例）
# 2、autouse
#   True：自动执行
#   False：手动执行， @pytest.mark.usefixtures("exe_sql")
# 3、params参数化，一般用在function里面，有正例反例时使用,数据是list格式或者是list of dict(字典列表)
#   需要在固件名中传入request参数，yield后面加上request.param，固定写法
# 4、ids 参数化之后对参数的别名，必须和params一起使用,不能单独使用
# 5、name是固件的别名，特别注意：一旦固件加了别名之后，那么就只能用别名，原来传递的参数名需要修改为别名。
