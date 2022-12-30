import asyncio
from logging import error

import bson

from common_services.entity import get_entities_page
from entity_pb2 import GetEntitiesPageRequest
from id_codes.manage_ids import MANAGES_MANAGE_ID
from knitter_client import get_knitter_client_stub, login
from test_settings import *


async def main():
    metadata, person= await login(area_code, phone, passwd, insecure_channel)

    client_stub = get_knitter_client_stub(channel=insecure_channel)
    request = GetEntitiesPageRequest(manage_id=MANAGES_MANAGE_ID, page_index = 1)

    ok, m_response, details = await get_entities_page(request, client_stub, metadata=metadata) 

    # 打印管理表
    if ok == grpc.StatusCode.OK:
        for entity in m_response.entities:
            print(bson.decode(entity))
    else:
        error("发生错误%s-%s"%(ok, details))
        return

    assert ok == grpc.StatusCode.OK
    # assert len(m_response.entity > 0

asyncio.run(main())

