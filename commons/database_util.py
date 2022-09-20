# -*- encoding：utf-8 -*-
# @Author: Kurosaki
# @Date Time: 2022/9/17 17:03
# @Filename: database_util
# @Description:
import pymysql


class DatabaseUtil:
    # 初始化数据库连接信息
    def __init__(self, *args, **kwargs):
        # 创建数据库链接
        self.sql = pymysql.connect(user="root",
                                   password="123456",
                                   host="localhost",
                                   database="students",
                                   port=3306)
        self.c = self.sql.cursor()  # 创建游标（新的会话）

    # 执行sql语句
    def execute_sql(self, sql):
        # 执行sql
        self.c.execute(sql)
        # 提取值，fetchall返回多行结果，fetchone返回单行结果
        value = self.c.fetchall()
        # 关闭连接
        self.c.close()
        self.sql.close()
        return value


# def creat_connection():
#     conn = pymysql.connect(
#         user="root",
#         password="123456",
#         host="localhost",
#         database="students",
#         port=3306
#     )
#     return conn
#
#
# # 执行sql语句
# def execute_sql(sql):
#     conn = creat_connection()
#     c = conn.cursor()
#     # 执行sql
#     c.execute(sql)
#     # 提取值，fetchall返回多行结果，fetchone返回单行结果
#     value = c.fetchall()
#     # 关闭连接
#     c.close()
#     conn.close()
#     return value


if __name__ == '__main__':
    # 创建数据库链接
    # sql = DatabaseUtil(
    #     user="root",
    #     password="123456",
    #     host="localhost",
    #     database="students",
    #     port=3306
    # )
    print(DatabaseUtil().execute_sql("select age from students where studentNO=1;"))
