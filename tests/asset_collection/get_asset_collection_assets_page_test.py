import asyncio
from logging import error

import bson
from common_services.country import new_country

from common_services.entity import edit_entity_field
from common_services.name import new_language_name
from id_codes.general_field_ids import OWNER_FIELD_ID
from id_codes.manage_ids import MANAGES_MANAGE_ID
from knitter_client import get_knitter_client_stub, login
from asset_collection_pb2 import GetAssetCollectionAssetsPageRequest
from knitter_services.asset_collection import get_asset_collection_assets_page, new_asset_collection
from name_pb2 import Name
from test_settings import *


async def main():
    metadata, person = await login(area_code, phone, passwd, insecure_channel)

    client_stub = get_knitter_client_stub(channel=insecure_channel)

    request = GetAssetCollectionAssetsPageRequest(
            collection_id = "1",
            page_index = 0,
    )

    ok, m_response, details = await get_asset_collection_assets_page(
        request, client_stub, metadata=metadata
    )

    # 打印管理表
    if ok == grpc.StatusCode.OK:
        for asset in m_response.assets:
            print(bson.decode(asset))
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
