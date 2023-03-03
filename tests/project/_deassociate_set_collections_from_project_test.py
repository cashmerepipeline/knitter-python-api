import asyncio
from logging import error

import bson

from common_services.entity import get_entity, mark_entity_removed
from id_codes.general_field_ids import NAME_MAP_FIELD_ID, OWNER_FIELD_ID
from id_codes.manage_ids import ASSETS_MANAGE_ID, GROUPS_MANAGE_ID, MANAGES_MANAGE_ID
from project_pb2 import DeassociateAssetCollectionsFromProjectRequest
from knitter_client import get_knitter_client_stub, login
from knitter_services.project import deassociate_set_collections_from_project
from test_settings import *


async def main():
    metadata, person = await login(area_code, phone, passwd, insecure_channel)

    client_stub = get_knitter_client_stub(channel=insecure_channel)

    ok, m_response, details = await _deassociate_set_collections_from_project(
        project_id="0", collection_ids=["0", "1"], stub=client_stub, metadata=metadata
    )

    # 打印管理表
    if ok == grpc.StatusCode.OK:
        print(m_response.result)
        assert m_response.result == "ok"
    else:
        error("发生错误%s-%s" % (ok, details))
        return

    assert ok == grpc.StatusCode.OK
    # assert len(m_response.entity > 0

    # reset value
    # request = RecoverRemovedEntityRequest(
    #     manage_id=MANAGES_MANAGE_ID,
    #     entity_id="10000"
    # )
    # ok, m_response, details = await recover_removed_entity(
    #     request, client_stub, metadata=metadata
    # )

asyncio.run(main())
