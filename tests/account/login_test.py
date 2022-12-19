#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
Project: cashmere_server
Creator: 闫刚
Create time: 2020-10-22 07:33
Introduction:
"""
import logging
import sys
import os
import asyncio
import bson
import grpc

from common_services.account import login
from login_pb2 import LoginRequest
from knitter_client import get_account_server_client
from test_settings import server, area_code, phone, passwd, insecure_channel

stub = get_account_server_client(insecure_channel)
request = LoginRequest( area_code=area_code, phone= phone, password=passwd)

ok, response, details = asyncio.run(login(request, stub))
if not ok == grpc.StatusCode.OK:
    logging.error("登录失败")
else:
    print(bson.decode(response.person))
    print(response.token)

assert ok == grpc.StatusCode.OK
