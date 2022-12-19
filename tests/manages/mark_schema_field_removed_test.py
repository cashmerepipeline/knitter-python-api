import asyncio
from logging import error, log

import bson

from common_services.manage import get_manage_entry_count, get_manage_schema, get_manages, mark_manage_schema_field_removed
from auth_codes import RoleGroupName
from id_codes.field_ids import MANAGES_SCHEMA_FIELD_ID
from id_codes.manage_ids import GROUPS_MANAGE_ID, MANAGES_MANAGE_ID
from knitter_client import get_knitter_client_stub,login
from test_settings import *

from manage_schema_pb2 import MarkSchemaFieldRemovedRequest, MarkSchemaFieldRemovedResponse


async def main():
    metadata, person= await login(area_code, phone, passwd, insecure_channel)
    client_stub = get_knitter_client_stub(channel=insecure_channel)

    # mark Manage schema field
    request = MarkSchemaFieldRemovedRequest(manage_id= MANAGES_MANAGE_ID, field_id = MANAGES_SCHEMA_FIELD_ID)

    ok, m_response, details = await mark_manage_schema_field_removed(request, stub=client_stub, metadata=metadata)
    if ok == grpc.StatusCode.OK:
        print(m_response)
    else:
        error("发生错误%s-%s"%(ok, details))
        return

    assert ok == grpc.StatusCode.OK
    assert m_response.result == "ok"

asyncio.run(main())
