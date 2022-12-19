import asyncio
from logging import log

import bson

from common_services.manage import get_manage_entry_count, get_manage_schema, get_manages
from auth_codes import RoleGroupName
from id_codes.manage_ids import GROUPS_MANAGE_ID, MANAGES_MANAGE_ID
from knitter_client import get_knitter_client_stub, login
from test_settings import *

from manage_schema_pb2 import GetManageSchemaRequest

async def main():
    metadata, person= await login(area_code, phone, passwd, insecure_channel)

    client_stub = get_knitter_client_stub(channel=insecure_channel)

    # get Manage schema
    request = GetManageSchemaRequest(manage_id=MANAGES_MANAGE_ID)

    ok, m_response, details = await get_manage_schema(request, client_stub, metadata=metadata)

    # 打印模式表
    if ok == grpc.StatusCode.OK:
        fields = map(lambda x: (x.id, bson.decode(x.name_map), x.data_type, x.removed), sorted(m_response.fields, key=lambda x: x.id))
        for field in fields:
            print(field)
    else:
        print("发生错误%s-%s"%(ok, details))
        return

    assert ok == grpc.StatusCode.OK
    assert len(m_response.fields) > 0

asyncio.run(main())
