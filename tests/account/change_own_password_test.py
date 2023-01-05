import asyncio
from logging import error

import bson
from common_services.account import change_own_password, new_account

from common_services.language_code import new_language_code
from knitter_client import get_account_server_client, get_knitter_client_stub, login
from account_pb2 import NewAccountRequest 
from password_pb2 import ChangeOwnPasswordRequest
from name_pb2 import Name
from test_settings import *


async def main():
    metadata, person = await login(area_code, phone, passwd, insecure_channel)

    client_stub = get_account_server_client(channel=insecure_channel)
    request = ChangeOwnPasswordRequest(
            old_password = "root",
            new_password = "123456"
            )

    ok, m_response, details = await change_own_password(
        request, client_stub, metadata=metadata
    )

    # 打印管理表
    if ok == grpc.StatusCode.OK:
        print(m_response.result)
    else:
        error("发生错误%s-%s" % (ok, details))
        return

    assert ok == grpc.StatusCode.OK
    # assert len(m_response.entity > 0

    # reset password
    request = ChangeOwnPasswordRequest(
            old_password = "123456",
            new_password = "root"
            )

    ok, m_response, details = await change_own_password(
        request, client_stub, metadata=metadata
    )
    assert ok == grpc.StatusCode.OK

asyncio.run(main())
