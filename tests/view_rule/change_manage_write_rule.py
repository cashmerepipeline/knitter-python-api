import asyncio

import bson

from common_services.manage import get_manage_entry_count, get_manages
from auth_codes import RoleGroupName
from common_services.view_rule import change_collection_write_rule, change_manage_write_rule
from id_codes.manage_ids import GROUPS_MANAGE_ID, MANAGES_MANAGE_ID
from knitter_client import get_knitter_client_stub, login
from test_settings import *

from view_pb2 import ChangeManageWriteRuleRequest


async def main():
    metadata, person= await login(area_code, phone, passwd, insecure_channel)

    client_stub = get_knitter_client_stub(channel=insecure_channel)

    # get manages count
    request = ChangeManageWriteRuleRequest(manage_id=MANAGES_MANAGE_ID, group_id="10001", write_rule="InVisible")

    ok, m_response, details = await change_manage_write_rule(
        request, client_stub, metadata=metadata
    )
    
    if ok == grpc.StatusCode.OK:
        print(m_response)
    else:
        print("发生错误%s-%s"%(ok, details))
        return

    assert ok == grpc.StatusCode.OK
    # assert m_response.count > 0

asyncio.run(main())



