#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/5/15 上午 02:33
import pytest
import requests
import random
from common.handle_config import conf
from common.handle_log import log


@pytest.fixture(scope='class')
def login_setup():
    url = conf.get("login", "url")
    params = {"UsernameOrEmailAddress": conf.get("login", "username"),
              "Password": conf.get("login", "password"),
              "RememberMe": "false",
              "TenancyName": "Default"}
    headers = {"cookie": "ASP.NET_SessionId=p1yeborxr4wql2yu0fyiaybe",
               "content-type": "application/json;charset=UTF-8"}
    # requests.adapters.DEFAULT_RETRIES = 5
    session = requests.session()
    # session.keep_alive = False
    response = session.post(url=url, json=params, headers=headers)
    log.error(response.text)
    yield session


@pytest.fixture(scope='class')
def project_side(login_setup):
    session_side = login_setup
    name = "上海科学技术有限责任公司{}".format(random.randint(0,100))
    url = r"https://chalseenew_pdm.icwn.cn/Api/services/app/ProjectSide/SaveProjectSide"
    params = {"Ownerships": [
        {"HolderName": "周海明", "subscriptionAmount": 1000, "amountPaidIn": 1000, "ContriWay": "现金", "ContriRatio": 100,
         "Member": ""}], "IsHighTech": 0, "CompanyName": name, "legalPerson": "周海明", "FoundDate": "2020-4-29",
              "RegiCapital": 10000, "isHighTech": 2, "Communicator": "赵其他", "ComunicateJob": "法务",
              "ComunicateTel": "13928883942", "Category": "制造业"}
    response = session_side.post(url=url, json=params)
    res = response.json()
    yield session_side, res["result"]["id"]
    session_side.close()
