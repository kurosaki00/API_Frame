# -*- encoding：utf-8 -*-
# @Author: Kurosaki
# @Date Time: 2022/9/22 22:29
# @Filename: test_all_cases
# @Description:
from pathlib import Path

import allure
import pytest
import yaml

from commons.ddt_util import read_testcase
from commons.request_util import RequestUtil

# 当前路径
current_path = Path(__file__).parent
# 找到所有的代表测试用例的yaml文件，**表示所有文件
yaml_case_list = current_path.glob("**/*.yaml")


# print(yaml_case_list)


class TestAllCases:
    pass


# 创建测试用例
def create_testcases(yaml_path):
    # 读取yaml文件,返回结果是一个列表
    with open(yaml_path, mode="r", encoding="utf-8") as f:
        caseinfo = yaml.safe_load(f)

    # # 判断yaml中的url是否以http开头,是的话不传入base_url
    # def judge_url(caseinfo, base_url):
    #     if caseinfo["request"]["url"].startswith("http"):
    #         RequestUtil().standard_yaml(caseinfo, "")
    #     else:
    #         RequestUtil().standard_yaml(caseinfo, base_url)

    # 用例
    @allure.feature(caseinfo[0]["feature"])
    @allure.story(caseinfo[0]["story"])
    # @allure.story(caseinfo[0]["title"])  # 会报错,因为有ddt数据驱动
    # @allure.title("{caseinfo[title]}")
    @pytest.mark.parametrize("caseinfo", read_testcase(yaml_path))
    # def test_func(self, caseinfo, base_url):
    def test_func(self, caseinfo):  # 热加载读取config.yaml基础路径，不需要再传入base_url
        # print(caseinfo["request"]["url"])
        # # 获取base_url基础路径
        # base_url=read_config_yaml("base_url")

        if not isinstance(caseinfo, list):  # 单接口用例
            allure.dynamic.title(caseinfo["title"])
            RequestUtil().standard_yaml(caseinfo)  # (caseinfo, base_url)
            # judge_url(caseinfo, base_url)
            # if caseinfo["request"]["url"].startswith("http"):
            #     RequestUtil().standard_yaml(caseinfo, "")
            # else:
            #     RequestUtil().standard_yaml(caseinfo, base_url)
        else:  # 流程用例，不能用数据驱动
            for case in caseinfo:
                allure.dynamic.title(case["title"])
                RequestUtil().standard_yaml(case)  # (case, base_url)
                # judge_url(case, base_url)
                # if case["request"]["url"].startswith("http"):
                #     RequestUtil().standard_yaml(case, "")
                # else:
                #     RequestUtil().standard_yaml(case, base_url)

    return test_func


# 循环所有的yaml用例的文件名
for yaml_path in yaml_case_list:
    # print(yaml_path)
    yaml_name = yaml_path.name[:-5]
    # print(yaml_name)
    setattr(TestAllCases, f"test_{yaml_name}", create_testcases(yaml_path))
