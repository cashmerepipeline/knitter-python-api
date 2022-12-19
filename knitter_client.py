import logging

import grpc
from grpc import Channel

import account_service_pb2_grpc
from auth_codes import RoleGroupName
from knitter_pb2_grpc import KnitterGrpcStub
from login_pb2 import LoginRequest

from common_services import account


def get_knitter_client_stub(channel: Channel):
    stub = KnitterGrpcStub(channel=channel)
    return stub


def get_account_server_client(channel: Channel):
    stub = account_service_pb2_grpc.AccountGrpcStub(channel)
    return stub


LOGIN_METADATA = None


async def login(area_code, phone, password, channel):
    global LOGIN_METADATA
    if LOGIN_METADATA:
        return LOGIN_METADATA

    request = LoginRequest(area_code=area_code, phone=phone, password=password)
    stub = get_account_server_client(channel)
    ok, response, details = await account.login(request, stub)
    if not ok == grpc.StatusCode.OK:
        logging.error("登录失败")
        logging.error(details)
    else:
        metadata = (
            ("authorization", "bearer %s" % response.token),
            (RoleGroupName, "10000"),
        )
        LOGIN_METADATA = (metadata, response.person)
        return LOGIN_METADATA
