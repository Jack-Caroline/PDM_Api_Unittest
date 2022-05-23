#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/5/16 下午4:26
import os
import pytest
import requests
import random

# from common.handle_excel import Excel
from common.handle_path import CASEDARAS_DIR

file_path = os.path.join(CASEDARAS_DIR, "pdm_test_data.xlsx")

case = {'case_id': 1, 'title': '登录成功', 'interface': 'login', 'method': 'post',
        'url': 'https://chalseenew_pdm.icwn.cn/Account/LoginSystem',
        'data': '{"UsernameOrEmailAddress": "admin",\n "Password": "fintech",\n "RememberMe": "false",\n "TenancyName": "Default"}',
        'expected': None}
# excel = Excel(file_path, "login")
# case = excel.read_data()
print(case)
url = case["url"]
params = eval(case["data"])
method = case["method"]
headers = {"cookie": "ASP.NET_SessionId=p1yeborxr4wql2yu0fyiaybe", "content-type": "application/json;charset=UTF-8"}
session_pdm = requests.Session()
response = session_pdm.post(url=url, json=params, headers=headers)
if response.text == "Success":
    print(True)
else:
    print(False)
print(type(response))
print(response)
print(response.text)
print(type(response.text))
print(response.cookies)
url1 = r"https://chalseenew_pdm.icwn.cn/Api/services/app/Project/CreateProject"
params1 = {
    "ProjectSideId": 101,
    "ProjectName": "模拟地产项目1号",
    "ProjectParticipants": [{
        "employeeId": 92,
        "name": "发行管理经理",
        "email": "123456@123",
        "job": "发行管理经理"
    }, {
        "employeeId": 94,
        "name": "产品经理",
        "email": "12345@123",
        "job": "产品经理"
    }, {
        "employeeId": 93,
        "name": "产品总监",
        "email": "123456@12",
        "job": "产品总监"
    }, {
        "employeeId": 95,
        "name": "项目总监",
        "email": "456@123",
        "job": "项目总监"
    }],
    "ProjectVersions": {
        "IsAuditStatements": "1",
        "FocusAttentions": [{
            "Matter": "退出方式",
            "FocusAttentionIndex": 0
        }, {
            "Matter": "股东人数是否超过200人",
            "FocusAttentionIndex": 1
        }, {
            "Matter": "历史沿革是否涉及国企或集体企业改革",
            "FocusAttentionIndex": 2
        }, {
            "Matter": "现有股东是否存在国有股东（包括国有控股的股权投资机构）、外资股东",
            "FocusAttentionIndex": 3
        }, {
            "Matter": "是否存在涉嫌出资不实的情形（重点关注无形资产出资、事务出资、自有资产评估增资等）",
            "FocusAttentionIndex": 4
        }, {
            "Matter": "是否存在你关联方大额资金占用或对关联方提供担保",
            "FocusAttentionIndex": 5
        }, {
            "Matter": "是否与控股股东、实际控制人存在同业竞争",
            "FocusAttentionIndex": 6
        }, {
            "Matter": "是否存在影响独立性的持续性关联交易",
            "FocusAttentionIndex": 7
        }, {
            "Matter": "是否存在账外收入及是否需要大额补税",
            "FocusAttentionIndex": 8
        }, {
            "Matter": "最近两年是否存在重大违法违规行为",
            "FocusAttentionIndex": 9
        }],
        "FinancialSituations": [{
            "Year": 2022,
            "TotalAssets": 2022,
            "TotalLiabilities": 2023,
            "NetAssets": 2024,
            "ActuralIncome": 2025,
            "ActuralNetProfit": 2026
        }, {
            "Year": 2021,
            "TotalAssets": 1021,
            "TotalLiabilities": 1022,
            "NetAssets": 1023,
            "ActuralIncome": 1024,
            "ActuralNetProfit": 1025
        }, {
            "Year": 2020
        }, {
            "Year": 2019
        }],
        "FinancingParty": "上海淑荣",
        "DatumReceiveTime": "2021-12-30",
        "FirstAuditor": "赵数禧",
        "ContectPhone": "13429384449",
        "ProjectType": "2",
        "ManageType": "2",
        "MainBusiness": "主营业务：模拟123",
        "CompetitiveEdge": "业务优势：456",
        "FinancingPlan": "融资用途：789",
        "AuditInstitutions": "上海数据中心",
        "ProjectNote": "注意事项：1、风控问题"
    }
}
response2 = session_pdm.post(url=url1, json=params1)
# res = res.replace("null", "\"null\"", res.count("null"))
# res = eval(res)
res = response2.json()
print(response2)
print(response2.text)
print(res)

# url1 = r"https://chalseenew_pdm.icwn.cn/Api/services/app/ProjectSide/SaveProjectSide"
# headers = {"cookie": "ASP.NET_SessionId=p1yeborxr4wql2yu0fyiaybe", "content-type": "application/json;charset=UTF-8"}
# params1 = {"Ownerships": [
#     {"HolderName": "周海明", "subscriptionAmount": 1000, "amountPaidIn": 1000, "ContriWay": "现金", "ContriRatio": 100,
#      "Member": ""}], "IsHighTech": 0, "CompanyName": "上海模拟科技有限公司01", "legalPerson": "周海明", "FoundDate": "2020-4-29",
#     "RegiCapital": 10000, "isHighTech": 2, "Communicator": "赵其他", "ComunicateJob": "法务",
#     "ComunicateTel": "13928883942", "Category": "制造业"}
# response2 = session_pdm.post(url=url1, json=params1)
# session_pdm.close()
# res = response2.text
# # res = res.replace("null", "\"null\"", res.count("null"))
# # res = eval(res)
# res = response2.json()
# print(response2)
# print(response2.text)
# print(res["result"]["companyName"])
# print(res["result"]["id"])

# session_log=requests.session()
# url1 = r"http://rycbstest.icwn.cn:2050/Systems/System/Login"
# params1 = {"UserName": "admin", "Password": "123456"}
# response2 = session_log.post(url=url1, json=params1)
# print(response2.json())
# print(response2.json()["Code"])
# login_cookies = response2.cookies
# print(login_cookies)
#
# url2 = r"http://rycbstest.icwn.cn:2050/Security/PasswordChangeRecord/ResetOtherPassword"
# params2 = {"userId": "cc251516-76b0-44c4-ba97-6d8d9ae31f81", "newPassword": "111111", "confirmPassword": "111111"}
# response3 = session_log.post(url=url2, json=params2)
# print(response3.json())
# print(response3.json()["Code"])
