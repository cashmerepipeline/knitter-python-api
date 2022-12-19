import asyncio
from logging import log

import bson

from common_services.manage import get_manage_entry_count, get_manages
from auth_codes import RoleGroupName
from id_codes.manage_ids import GROUPS_MANAGE_ID, MANAGES_MANAGE_ID
from knitter_client import get_knitter_client_stub, login
from test_settings import *

from manage_pb2 import GetManageEntryCountRequest


async def main():
    metadata, person= await login(area_code, phone, passwd, insecure_channel)

    client_stub = get_knitter_client_stub(channel=insecure_channel)

    # get manages count
    request = GetManageEntryCountRequest(manage_id=MANAGES_MANAGE_ID)

    ok, m_response, details = await get_manage_entry_count(
        request, client_stub, metadata=metadata
    )
    
    if ok == grpc.StatusCode.OK:
        print(m_response)
    else:
        print("发生错误%s-%s"%(ok, details))
        return


    assert ok == grpc.StatusCode.OK
    assert m_response.count > 0

asyncio.run(main())
