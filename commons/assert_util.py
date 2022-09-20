# -*- encoding：utf-8 -*-
# @Author: Kurosaki
# @Date Time: 2022/9/16 23:42
# @Filename: assert_util
# @Description: 断言封装
import logging

# 两个参数，一个预期结果，一个实际结果
import jsonpath

# 总的断言方法
from commons.database_util import DatabaseUtil

logger = logging.getLogger(__name__)


def assert_result(validate, res):
    # 对字典进行循环判断
    for key, value in validate.items():
        if key == 'codes':
            # print("状态码")
            # print(f'res.status_code{res.status_code}')
            assert_codes(value, res.status_code)
        elif key == 'equals':
            # print("相等")
            assert_equals(value, res.json())
        elif key == 'contains':
            # print("包含")
            # 包含断言一般用text
            assert_contains(value, res.text)
        elif key == 'databases':
            # print("数据库")
            # 数据库断言一般用json格式
            assert_databases(value, res.json())
        else:
            logger.info("不支持的断言")


# 抛出断言异常的方法
def raise_assert_error(msg):
    logger.info(msg)
    logger.info("----------测试用例请求结束----------\n")
    raise AssertionError(msg)


def assert_codes(yq_code, sj_code):
    if yq_code != sj_code:
        # print(f'断言失败，预期为{yq_code},实际为{sj_code}')
        raise_assert_error(f'断言失败，预期为{yq_code},实际为{sj_code}')
    # else:  # 相等不一定代表成功
    #     print('codes断言成功')


def assert_equals(yq_value, sj_json_value):
    for key, value in yq_value.items():
        # 在实际结果中查找有没有预期断言的key，可能有多个值，存储在列表里,用jsonpath在实际结果中查找key的value
        # "$..%s" % key表示在json中递归查找key为（%s）的值，..代表多层，.代表根目录
        list_result = jsonpath.jsonpath(sj_json_value, "$..%s" % key)
        # print(list_result)
        if list_result:
            # 如果查找结果列表里没有value，断言失败
            if value not in list_result:
                # print(f'equals断言失败，{key}不等于预期结果{value}')
                raise_assert_error(f'equals断言失败，{key}不等于预期结果{value}')
                # raise AssertionError(f'equals断言失败，{key}不等于预期结果{value}')
            # else:
            #     print(f"equals断言成功，预期结果为{yq_value}，实际结果为‘{key}：{value}’")
        else:  # 列表为空，没有预期key
            raise_assert_error(f'equals断言失败，返回结果中没有：{key}')


def assert_contains(yq_data, sj_text_value):
    # yq_data可能是整型，需要进行强转
    if str(yq_data) not in sj_text_value:
        raise AssertionError(f'contains断言失败，返回结果中不包含预期结果{yq_data}')
    # else:
    #     print(f"contains断言成功，实际结果中包含预期结果{yq_data}’")


# 数据库断言,涉及到增删改查核心业务、流程用例、统计接口时使用，两个第三方模块pymysql、mysqlclient（基于C语言的）处理
def assert_databases(yq_data, sj_json_data):
    for key, sql in yq_data.items():
        # print(key, sql)
        list_result = jsonpath.jsonpath(sj_json_data, "$..%s" % key)
        # print(list_result)
        if list_result:
            try:
                select_result = DatabaseUtil().execute_sql(sql)
            except:
                raise AssertionError(f'database断言失败，sql查询异常，请检查sql语句')
            else:
                # 如果select_result长度为0代表没查询要结果
                if len(select_result) == 0:
                    raise AssertionError(f'database断言失败，sql没有查询到结果')
                else:
                    # print(list_result[0])  #[0]
                    # print(select_result[0][0])   #((0,),)
                    if list_result[0] not in select_result[0]:
                        # print(f'database断言失败，实际结果{select_result[0]}不等于预期结果{list_result[0]}')
                        raise AssertionError(
                            f'database断言失败，实际结果{select_result[0]}不等于预期结果{list_result[0]}')

        else:
            raise AssertionError(f'database断言失败，返回结果中没有：{key}')
