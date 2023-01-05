import asyncio
from logging import error

import bson

from common_services.entity import edit_entity_field
from common_services.name import new_language_name
from id_codes.field_ids import CUTS_REFERENCES_FIELD_ID
from id_codes.general_field_ids import OWNER_FIELD_ID
from id_codes.manage_ids import CUTS_MANAGE_ID, MANAGES_MANAGE_ID
from knitter_client import get_knitter_client_stub, login
from knitter_services.prefabs import new_prefab
from knitter_services.reference import add_references
from reference_pb2 import ReferenceType, Reference, AddReferencesRequest
from name_pb2 import Name
from test_settings import *


async def main():
    metadata, person = await login(area_code, phone, passwd, insecure_channel)

    client_stub = get_knitter_client_stub(channel=insecure_channel)
    ref1 = Reference(
            reference_type = ReferenceType.RefAsset,
            source_id = "1",
            specs_id = "0",
            prefab_id = "basic"
            )
    refs = list()
    refs.append(ref1)
    request = AddReferencesRequest(
        subject_manage_id = CUTS_MANAGE_ID,
        subject_entity_id = "0",
        reference_field_id = str(CUTS_REFERENCES_FIELD_ID),
        references = [ref1]
    )

    ok, m_response, details = await add_references(
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




