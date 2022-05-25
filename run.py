#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/5/15 上午 02:33

import unittest
import os
from common.handle_path import TESTCASES_DIR,REPORTS_DIR
from unittestreport import TestRunner
from common.handle_config import conf

# 加载套件
suite = unittest.defaultTestLoader.discover(TESTCASES_DIR)

# 执行测试用例
runner = TestRunner(suite,
                    filename=conf.get("report", "filename"),
                    report_dir=REPORTS_DIR,
                    title="接口测试报告",
                    tester="老金",
                    desc="老金的测试报告",
                    templates=1
                    )

# 运行
runner.run()

# 运行失败后重新运行(失败后，等待3秒，循环2次)
# runner.rerun_run(count=2,interval=3)

# 发送测试报告到邮箱
runner.send_email(
    host="smtp.qq.com",
    port=465,
    user="jinshaokai11@foxmail.com",
    password="pflezxzclfckbbdd",
    to_addrs="jinshaokai11@foxmail.com"
)