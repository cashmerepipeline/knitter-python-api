import asyncio
from logging import log

import bson

from common_services.manage import get_manage_entry_count, get_manage_schema, get_manages
from auth_codes import RoleGroupName
from id_codes.manage_ids import GROUPS_MANAGE_ID, MANAGES_MANAGE_ID
from knitter_client import get_client_stub
from common_services.account.login import login
from test_settings import *

from manage_schema_pb2 import GetManageSchemaRequest, GetManageSchemaResponse


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

    # get Manage schema
    request = GetManageSchemaRequest(manage_id=MANAGES_MANAGE_ID)

    ok, m_response, details = await get_manage_schema(request, client_stub, metadata=metadata)

    # 打印模式表
    if ok == grpc.StatusCode.OK:
        fields = map(lambda x: (x.id, bson.decode(x.name_map), x.data_type), sorted(m_response.fields, key=lambda x: x.id))
        for field in fields:
            print(field)
    else:
        print("发生错误%s-%s"%(ok, details))
        return

    assert ok == grpc.StatusCode.OK
    assert len(m_response.fields) > 0

asyncio.run(main())
