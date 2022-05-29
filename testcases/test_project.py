#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/5/15 上午 02:33
import unittest
import os
import requests
import random
from common.handle_excel import Excel
from common.handle_path import CASEDARAS_DIR
from common.handle_log import log
from common import myddt
from common.handle_config import conf

file_path = os.path.join(CASEDARAS_DIR, "pdm_test_data.xlsx")


@myddt.ddt
class TestProject(unittest.TestCase):
    excel = Excel(file_path, "project")
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
        project_side_name = "上海科学技术有限责任公司{}".format(random.randint(0, 100))
        project_url = r"https://chalseenew_pdm.icwn.cn/Api/services/app/ProjectSide/SaveProjectSide"
        project_params = {"Ownerships": [
            {"HolderName": "周海明", "subscriptionAmount": 1000, "amountPaidIn": 1000, "ContriWay": "现金",
             "ContriRatio": 100,
             "Member": ""}], "IsHighTech": 0, "CompanyName": project_side_name, "legalPerson": "周海明", "FoundDate": "2020-4-29",
            "RegiCapital": 10000, "isHighTech": 2, "Communicator": "赵其他", "ComunicateJob": "法务",
            "ComunicateTel": "13928883942", "Category": "制造业"}
        response_project_side = session.post(url=project_url, json=project_params)
        global cookies,project_side_id
        cookies = session.cookies
        project_side_id = response_project_side.json()["result"]["id"]
        log.error(response.text)

    @myddt.data(*cases)
    def test_project(self, item):
        url = item["url"]
        # method = item["method"]
        params = eval(item["data"])
        params["ProjectSideId"] = project_side_id
        response = requests.post(url=url, json=params, cookies=cookies)
        try:
            assert response.json()["success"] == True
        except Exception as e:
            log.error("测试用例{}，执行失败".format(item["title"]))
            log.exception(e)
            raise e
        else:
            log.error("测试用例{}，执行成功".format(item["title"]))
