import asyncio
from logging import error

import bson
from common_services.country import new_country

from common_services.entity import edit_entity_field
from common_services.name import new_language_name
from id_codes.general_field_ids import OWNER_FIELD_ID
from id_codes.manage_ids import MANAGES_MANAGE_ID
from knitter_client import get_knitter_client_stub, login
from knitter_services.cut import new_cut
from cut_pb2 import NewCutRequest
from knitter_services.asset import new_asset
from knitter_services.asset_collection import new_asset_collection
from knitter_services.epic import new_epic
from knitter_services.project import new_project
from name_pb2 import Name
from test_settings import *


async def main():
    metadata, person = await login(area_code, phone, passwd, insecure_channel)

    client_stub = get_knitter_client_stub(channel=insecure_channel)
    name = Name(language="zh", name="测试镜头")
    request = NewCutRequest(
        name=name,
        sequence_id="1",
        description="test new cut"
    )

    ok, m_response, details = await new_cut(
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
    # request = NewLanguageNameRequest(
    #     manage_id=MANAGES_MANAGE_ID,
    #     entity_id="10000",
    #     language='ru',
    #     new_name= None
    # )
    # await new_language_name(request, client_stub, metadata=metadata)


asyncio.run(main())





