import pytest
import time
import os

from commons.yaml_util import read_yaml

if __name__ == '__main__':
    pytest.main()
    # time.sleep(1)
    # 生成html的allure报告
    os.system("allure generate ./temps -o ./reports --clean")  # 通过临时文件temps输出到reports，每次执行前--clean先清空上次报告
    # print(read_yaml())
    # 保留历史报告
    # files_name = "./reports/report_"+str(int(time.time()))
    # files_name = f'./reports/report_{str(int(time.time()))}'
    # print(file_name)
    # os.mkdir(files_name)
    # time.sleep(3)
    # os.system("allure generate ./temps -o "+files_name+" --clean")
    # os.system(f 'allure generate ./temps -o {files_name} --clean')

# 生成局域网报告,在Terminal下执行命令 allure open ./reports

"""
异常处理：
1、try...except——捕获异常进行处理，Allure报告显示用例通过
2、raise抛出异常，抛出除了断言异常以外的所有异常，Allure报告显示用例故障
3、raise抛出异常，抛出除了断言异常，Allure报告显示用例失败
"""
