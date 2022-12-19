import pytest
import asyncio
from logging import error, info
import bson

from common_services.manage import get_manages
from auth_codes import RoleGroupName
from knitter_client import get_knitter_client_stub, login
from test_settings import *
import manage_pb2

async def main():
    metadata, person= await login(area_code, phone, passwd, insecure_channel)

    client_stub = get_knitter_client_stub(channel=insecure_channel)
    request = manage_pb2.GetManagesRequest()

    ok, m_response, details = await get_manages(request, client_stub, metadata=metadata) 

    # 打印管理表
    if ok == grpc.StatusCode.OK:
        manages = map(lambda x: (x.manage_id, bson.decode(x.name_map)), sorted(m_response.manages, key=lambda x: x.manage_id))
        info("get %d manages:" %len(m_response.manages))
        for manage in manages:
            print(manage)
    else:
        error("发生错误%s-%s"%(ok, details))
        return

    assert ok == grpc.StatusCode.OK
    assert len(m_response.manages) > 0

asyncio.run(main())

