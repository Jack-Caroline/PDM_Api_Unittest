#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/5/15 上午 02:33
import os
import logging
from logging.handlers import TimedRotatingFileHandler
from common.handle_path import LOG_DIR
from common.handle_config import conf


class HandlerLog:

    @staticmethod
    def create_log():
        log = logging.getLogger("jack")
        log.setLevel(conf.get("logging", "level"))

        fh = TimedRotatingFileHandler(os.path.join(LOG_DIR, conf.get("logging", "log_name")), when='d', interval=1,
                                      backupCount=7, encoding="utf-8")
        fh.setLevel(conf.get("logging", "fh_level"))
        log.addHandler(fh)

        sh = logging.StreamHandler()
        sh.setLevel(conf.get("logging", "sh_level"))
        log.addHandler(sh)

        formatter = "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
        mate = logging.Formatter(formatter)

        fh.setFormatter(mate)
        sh.setFormatter(mate)
        return log


log = HandlerLog.create_log()
