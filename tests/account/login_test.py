#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
Project: cashmere_server
Creator: 闫刚
Create time: 2020-10-22 07:33
Introduction:
"""

import sys
import os
import asyncio

sys.path.append(".")
sys.path.append("./grpc_generated")
sys.path.append(os.path.dirname(__file__))

import bson
import grpc

from common_services.account.login import login

from test_settings import server, country_code, phone, passwd

ok, response, details = asyncio.run(login(server, country_code, phone, passwd))

assert ok == grpc.StatusCode.OK