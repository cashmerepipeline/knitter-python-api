#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
Project: cashmere_python_client
Creator: 闫刚
Create time: 2020-10-27 11:00
Introduction:
"""

import grpc
from login_pb2 import LoginRequest
import account_service_pb2_grpc

async def login(request:LoginRequest, stub):
    """

    """
    try:
        response = stub.Login(request)
        return (grpc.StatusCode.OK, response, None)

    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

async def new_account(request, stub, metadata):
    try:
        response = stub.NewAccount(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

async def add_account_into_group(request, stub, metadata):
    try:
        response = stub.AddAccountIntoGroup(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

async def remove_account_from_group(request, stub, metadata):
    try:
        response = stub.RemoveAccountFromGroup(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

async def change_own_password(request, stub, metadata):
    try:
        response = stub.ChangeOwnPassword(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

async def change_account_status(request, stub, metadata):
    try:
        response = stub.ChangeAccountStatus(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

async def change_account_password(request, stub, metadata):
    try:
        response = stub.ChangeAccountPassword(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())