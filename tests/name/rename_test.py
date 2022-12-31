import asyncio
from logging import error

import bson

from common_services.name import rename
from name_pb2 import RenameRequest
from id_codes.general_field_ids import OWNER_FIELD_ID
from id_codes.manage_ids import MANAGES_MANAGE_ID
from knitter_client import get_knitter_client_stub, login
from test_settings import *


async def main():
    metadata, person = await login(area_code, phone, passwd, insecure_channel)

    client_stub = get_knitter_client_stub(channel=insecure_channel)
    new_value = dict({str(OWNER_FIELD_ID): "8610000000001"})
    request = RenameRequest(
        manage_id=MANAGES_MANAGE_ID,
        entity_id="10000",
        language='zh',
        new_name=str('测试新名称')
    )

    ok, m_response, details = await rename(
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
    request = RenameRequest(
        manage_id=MANAGES_MANAGE_ID,
        entity_id="10000",
        language='zh',
        new_name="管理",
    )
    await rename(request, client_stub, metadata=metadata)


asyncio.run(main())

