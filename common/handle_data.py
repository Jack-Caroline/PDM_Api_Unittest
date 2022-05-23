#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/5/15 上午 02:33
import random


# from common.handle_db import db


def random_phone(res):
    # 随机手机号
    res = res
    while res:
        phone = "154"
        for i in range(8):
            phone += str(random.randint(0, 9))
        print(phone)
        res -= 1
        # sql = "select * from xxx where phone={}".format(phone)
        # res = db.find_data(sql)

    return phone


# if __name__ == '__main__':
#     print(random_phone(5))