import asyncio
from logging import log
import sys
import os
sys.path.append(".")
sys.path.append("./grpc_generated")
sys.path.append(os.path.dirname(__file__))

import bson

from common_services.manage import get_manage_entry_count, get_manages
from auth_codes import RoleGroupName
from knitter_client import get_client_stub
from common_services.account.login import login
from test_settings import *

from manage_pb2 import GetManagesRequest, GetManageEntryCountRequest

async def main():
    ok, response, details = await login(server, country_code, phone, passwd)
    token = response.token

    metadata = (
        ("authorization", "bearer %s" % token),
        ("role_group", "10000"),
    )

    client_stub = get_client_stub(channel=insecure_channel)
     # groups
    request = GetManageEntryCountRequest(manage_id=100001)

    ok, m_response, details = await get_manage_entry_count(request, client_stub, metadata=metadata) 
    # resp = client_stub.GetManageEntryCount(request, metadata=metadata)

    print(m_response)

    assert m_response.count > 0

asyncio.run(main())


