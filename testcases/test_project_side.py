#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/5/15 上午 02:33

import os, json
import unittest
import requests
from common.handle_excel import Excel
from common.handle_path import CASEDARAS_DIR
from common.handle_log import log
from common import myddt
from common.handle_config import conf

file_path = os.path.join(CASEDARAS_DIR, "pdm_test_data.xlsx")


@myddt.ddt
class TestProjectSide(unittest.TestCase):
    excel = Excel(file_path, "side")
    cases = excel.read_data()

    @classmethod
    def setUpClass(cls) -> None:
        url = conf.get("login", "url")
        params = {"UsernameOrEmailAddress": conf.get("login", "username"),
                  "Password": conf.get("login", "password"),
                  "RememberMe": "false",
                  "TenancyName": "Default"}
        headers = {"cookie": "ASP.NET_SessionId=p1yeborxr4wql2yu0fyiaybe",
                   "content-type": "application/json;charset=UTF-8"}
        session = requests.session()
        response = session.post(url=url, json=params, headers=headers)
        global cookies
        cookies = session.cookies
        log.error(response.text)

    @myddt.data(*cases)
    def test_project_side(self, item):
        url = item["url"]
        method = item["method"]
        params = eval(item["data"])
        expected = item["expected"]
        response = requests.post(url=url, json=params, cookies=cookies)
        try:
            assert expected == response.json()["result"]["companyName"]
        except Exception as e:
            log.error("测试用例{}，执行失败".format(item["title"]))
            log.exception(e)
            raise e
        else:
            log.error("测试用例{}，执行成功".format(item["title"]))
