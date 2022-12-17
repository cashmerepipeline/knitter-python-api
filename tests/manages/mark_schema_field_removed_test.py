import asyncio
from logging import error, log

import bson

from common_services.manage import get_manage_entry_count, get_manage_schema, get_manages, mark_manage_schema_field_removed
from auth_codes import RoleGroupName
from id_codes.field_ids import MANAGES_SCHEMA_FIELD_ID
from id_codes.manage_ids import GROUPS_MANAGE_ID, MANAGES_MANAGE_ID
from knitter_client import get_client_stub
from common_services.account.login import login
from test_settings import *

from manage_schema_pb2 import MarkSchemaFieldRemovedRequest, MarkSchemaFieldRemovedResponse


async def main():
    ok, response, details = await login(server, country_code, phone, passwd)
    if not ok == grpc.StatusCode.OK:
        error("登录失败", ok, details)
        return -1

    token = response.token
    metadata = (
        ("authorization", "bearer %s" % token),
        (RoleGroupName, "10000"),
    )

    client_stub = get_client_stub(channel=insecure_channel)

    # get Manage schema
    request = MarkSchemaFieldRemovedRequest(manage_id= MANAGES_MANAGE_ID, field_id = MANAGES_SCHEMA_FIELD_ID)

    ok, m_response, details = await mark_manage_schema_field_removed(request, stub=client_stub, metadata=metadata)
    if ok == grpc.StatusCode.OK:
        print(m_response)
    else:
        error("发生错误%s-%s"%(ok, details))
        return


    assert ok == grpc.StatusCode.OK
    assert len(m_response.fields) > 0

asyncio.run(main())
