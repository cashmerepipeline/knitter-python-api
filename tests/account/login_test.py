#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
Project: cashmere_server
Creator: 闫刚
Create time: 2020-10-22 07:33
Introduction:
"""

import sys
sys.path.append(".")
sys.path.append("./grpc_generated")

import bson
import grpc
# from account_pb2 import Login, LoginRequest, LoginResponse
# import account_pb2_grpc

from common_services.account.login import login

country_code = "86"
phone = "10000000000"
passwd = "root"

server = "127.0.0.1:8800"
channel = grpc.insecure_channel(server)

ok, response, details = login(server, country_code, phone, passwd)
print(ok, response, details)
# print(response.token)
print(bson.decode(response.person))