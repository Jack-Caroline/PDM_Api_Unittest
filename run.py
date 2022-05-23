#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/5/15 上午 02:33

import pytest
import os

allure_report_path = "--alluredir=reports"
pytest.main([allure_report_path])
os.system("allure serve report")