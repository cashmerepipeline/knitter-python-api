import asyncio
from logging import error

import bson

from common_services.entity import edit_entity_array_field_remove_items
from id_codes.general_field_ids import GROUPS_FIELD_ID
from id_codes.manage_ids import ACCOUNTS_MANAGE_ID
from entity_pb2 import EditEntityArrayFieldRemoveItemsRequest
from knitter_client import get_knitter_client_stub, login
from test_settings import *


async def main():
    metadata, person = await login(area_code, phone, passwd, insecure_channel)

    client_stub = get_knitter_client_stub(channel=insecure_channel)
    new_value = dict({str(GROUPS_FIELD_ID): ["10002", "10003"]})
    request = EditEntityArrayFieldRemoveItemsRequest(
        manage_id=ACCOUNTS_MANAGE_ID,
        entity_id="8610000000000",
        field_id=str(GROUPS_FIELD_ID),
        items=bson.encode(document=new_value),
    )

    ok, m_response, details = await edit_entity_array_field_remove_items(
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
    # new_value = dict({str(OWNER_FIELD_ID): "8610000000000"})
    # request = EditEntityFieldRequest(
    #     manage_id=MANAGES_MANAGE_ID,
    #     entity_id="10000",
    #     field_id=str(OWNER_FIELD_ID),
    #     new_value=bson.encode(document=new_value),
    # )
    # await edit_entity_field(request, client_stub, metadata=metadata)


asyncio.run(main())
