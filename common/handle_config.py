#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/5/15 上午 02:33
import os
from configparser import ConfigParser
from common.handle_path import CONF_DIR


class Conf(ConfigParser):

    def __init__(self, filename, encoding='utf-8'):
        super().__init__()
        self.read(filename, encoding=encoding)


conf = Conf(os.path.join(CONF_DIR, "config.ini"))

