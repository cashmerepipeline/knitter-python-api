import asyncio
import sys
import os

sys.path.append(".")
sys.path.append("./grpc_generated")
sys.path.append(os.path.dirname(__file__))

import bson

from common_services.manage import get_manages
from auth_codes import RoleGroupName
from knitter_client import get_knitter_client_stub, login
from test_settings import *

from manage_pb2 import GetManagesRequest

async def main():
    metadata, person= await login(area_code, phone, passwd, insecure_channel)

    client_stub = get_knitter_client_stub(channel=insecure_channel)
    request = GetManagesRequest()

    ok, m_response, details = await get_manages(request, client_stub, metadata) 
    # resp = client_stub.GetManageEntryCount(request, metadata=metadata)

    # print(m_response.manages)
    if ok == grpc.StatusCode.OK:
        manages = map(lambda x: (x.manage_id, bson.decode(x.name_map)), sorted(m_response.manages, key=lambda x: x.manage_id))
        for manage in manages:
            print(manage)

    assert ok == grpc.StatusCode.OK

asyncio.run(main())
