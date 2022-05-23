#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/5/15 上午 02:33
import pymysql
from common.handle_config import conf


class DB():
    def __init__(self, host, port, user, password):
        self.con = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            charset="utf-8",
            cursorclass=pymysql.cursors.DictCursor
        )
        # 创建游标
        self.cur = self.con.cursor()

    def find_data(self, sql):
        # 查询数据
        self.cur.execute(sql)
        res = self.cur.fetchall()
        return res

    def updata_data(self, sql):
        # 修改数据，提交事务
        self.cur.execute(sql)
        self.con.commit()

    def close_data(self):
        # 关闭游标，关闭数据库
        self.cur.close()
        self.con.close()


db = DB(conf.get("mysql", "host"),
        int(conf.get("mysql", "port")),
        conf.get("mysql", "user"),
        conf.get("mysql", "password"), )
