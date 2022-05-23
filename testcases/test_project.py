#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/5/15 上午 02:33
import pytest
import os
from common.handle_excel import Excel
from common.handle_path import CASEDARAS_DIR
from common.handle_log import log

file_path = os.path.join(CASEDARAS_DIR, "pdm_test_data.xlsx")


class TestProject():
    excel = Excel(file_path, "project")
    cases = excel.read_data()

    @pytest.mark.parametrize("item", cases)
    def test_project(self, project_side, item):
        session_side, project_side_id = project_side
        url = item["url"]
        # method = item["method"]
        params = eval(item["data"])
        params["projectside"] = project_side_id
        # expected = item["expected"]
        response = session_side.post(url=url, json=params)
        try:
            assert response.json()["success"] == True
        except Exception as e:
            log.error("测试用例{}，执行失败".format(item["title"]))
            log.exception(e)
            raise e
        else:
            log.error("测试用例{}，执行成功".format(item["title"]))
