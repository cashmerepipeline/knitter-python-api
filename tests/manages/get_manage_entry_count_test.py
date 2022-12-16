import asyncio
from logging import log

import bson

from common_services.manage import get_manage_entry_count, get_manages
from auth_codes import RoleGroupName
from id_codes.manage_ids import GROUPS_MANAGE_ID, MANAGES_MANAGE_ID
from knitter_client import get_client_stub
from common_services.account.login import login
from test_settings import *

from manage_pb2 import GetManagesRequest, GetManageEntryCountRequest


async def main():
    ok, response, details = await login(server, country_code, phone, passwd)
    if not ok == grpc.StatusCode.OK:
        print("登录失败")
        print(details)
        return -1

    token = response.token
    metadata = (
        ("authorization", "bearer %s" % token),
        (RoleGroupName, "10000"),
    )

    client_stub = get_client_stub(channel=insecure_channel)
    # groups
    request = GetManageEntryCountRequest(manage_id=MANAGES_MANAGE_ID)

    ok, m_response, details = await get_manage_entry_count(
        request, client_stub, metadata=metadata
    )

    print(m_response)

    assert m_response.count > 0


asyncio.run(main())
