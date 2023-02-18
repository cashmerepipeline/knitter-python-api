import asyncio
from logging import error

import bson
from common_services.account import change_account_status, change_own_password, new_account

from common_services.language_code import new_language_code
from knitter_client import get_account_server_client, get_knitter_client_stub, login
from account_pb2 import ChangeAccountStatusRequest 
from account_status_pb2 import AccountStatus
from name_pb2 import Name
from test_settings import *


async def main():
    metadata, person = await login(area_code, phone, passwd, insecure_channel)

    client_stub = get_account_server_client(channel=insecure_channel)
    request = ChangeAccountStatusRequest(
            account_id = "8615147796961",
            status = AccountStatus.AccountStopped
            )

    ok, m_response, details = await change_account_status(
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
    request = ChangeAccountStatusRequest(
            account_id = "8615147796961",
            status = AccountStatus.AccountActived
            )

    ok, m_response, details = await change_account_status(
        request, client_stub, metadata=metadata
    )
    assert ok == grpc.StatusCode.OK

asyncio.run(main())

