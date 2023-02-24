import asyncio
from logging import error

import bson

from common_services.entity import edit_entity_field, edit_entity_map_field, get_entity
from id_codes.general_field_ids import NAME_MAP_FIELD_ID, OWNER_FIELD_ID
from id_codes.manage_ids import MANAGES_MANAGE_ID
from entity_pb2 import EditEntityMapFieldRequest
from knitter_client import get_knitter_client_stub, login
from test_settings import *


async def main():
    metadata, person = await login(area_code, phone, passwd, insecure_channel)

    client_stub = get_knitter_client_stub(channel=insecure_channel)
    new_value = dict({"zh": "编辑测试"})
    request = EditEntityMapFieldRequest(
        manage_id=MANAGES_MANAGE_ID,
        entity_id="10000",
        field_id=str(NAME_MAP_FIELD_ID),
        key="zh",
        new_value=bson.encode(document=new_value),
    )

    ok, m_response, details = await edit_entity_map_field(
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
    new_value = dict({"zh": "管理"})
    request = EditEntityMapFieldRequest(
        manage_id=MANAGES_MANAGE_ID,
        entity_id="10000",
        field_id=str(NAME_MAP_FIELD_ID),
        key="zh",
        new_value=bson.encode(document=new_value),
    )
    await edit_entity_field(request, client_stub, metadata=metadata)


asyncio.run(main())
