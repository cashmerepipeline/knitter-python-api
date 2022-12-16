#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
Project: cashmere_python_client
Creator: 闫刚
Create time: 2020-10-27 11:00
Introduction:
"""

import grpc
import login_pb2
import account_service_pb2_grpc

async def login(server, country_code, phone, password):
    """

    """
    channel = grpc.insecure_channel(server)
    stub = account_service_pb2_grpc.AccountGrpcStub(channel)
    try:
        response = stub.Login(login_pb2.LoginRequest(country_code=country_code, phone=phone, password=password))
        return (grpc.StatusCode.OK, response, None)

    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())
