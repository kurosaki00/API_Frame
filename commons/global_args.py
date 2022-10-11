# -*- encoding：utf-8 -*-
# @Author: Kurosaki
# @Date Time: 2022/9/20 22:37
# @Filename: global_arg
# @Description:
from pathlib import Path

from iniconfig import IniConfig

def load_ini():
    # 判断pytest.ini文件是否存在
    path = Path("./pytest.ini")
    if not path.exists():
        return {}
    # 判断[apitest]是否存在
    ini = IniConfig("./pytest.ini")
    # print(ini,type(ini))
    if "apitest" not in ini:
        return {}
    return dict(ini["apitest"].items())


if __name__ == '__main__':
    print(load_ini())
