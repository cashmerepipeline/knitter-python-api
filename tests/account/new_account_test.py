import asyncio
from logging import error

import bson
from common_services.account import new_account

from common_services.language_code import new_language_code
from knitter_client import get_account_server_client, get_knitter_client_stub, login
from account_pb2 import NewAccountRequest 
from name_pb2 import Name
from test_settings import *


async def main():
    metadata, person = await login(area_code, phone, passwd, insecure_channel)

    client_stub = get_account_server_client(channel=insecure_channel)
    name = Name(language="zh", name="测试账号")
    request = NewAccountRequest(
        nick_name=name,
        area_code="86",
        phone = "15147796961",
        password="15147796961"
    )

    ok, m_response, details = await new_account(
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

    # reset value
    # request = NewLanguageNameRequest(
    #     manage_id=MANAGES_MANAGE_ID,
    #     entity_id="10000",
    #     language='ru',
    #     new_name= None
    # )
    # await new_language_name(request, client_stub, metadata=metadata)


asyncio.run(main())
