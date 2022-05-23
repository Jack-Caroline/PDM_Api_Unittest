#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/5/15 上午 02:33
import os
import pytest
import requests
from common.handle_excel import Excel
from common.handle_path import CASEDARAS_DIR
from common.handle_log import log

file_path = os.path.join(CASEDARAS_DIR, "pdm_test_data.xlsx")


class TestLoin():
    excel = Excel(file_path, "login")
    cases = excel.read_data()

    @pytest.mark.parametrize('item', cases)
    def test_login(self, item):

        url = item["url"]
        params = eval(item["data"])
        method = item["method"]
        expected = item["expected"]
        headers = {"cookie": "ASP.NET_SessionId=p1yeborxr4wql2yu0fyiaybe",
                   "content-type": "application/json;charset=UTF-8"}
        response = requests.request(method, url=url, json=params,headers=headers)
        res = response.text
        try:
            assert expected == res
        except Exception as e:
            log.error("用例{}，执行未通过,{}".format(item["title"], res))
            log.exception(e)
            raise e
        else:
            log.error("用例{},执行通过".format(item["title"]))

