import grpc

from grpc_generated.knitter_pb2_grpc import KnitterGrpcStub
from entity_pb2 import MarkEntityRemovedRequest
from id_codes.manage_ids import PREFABS_MANAGE_ID

# 新预制件
async def new_prefab(request, stub: KnitterGrpcStub, metadata):
    try:
        response = stub.NewPrefab(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

# 标记移除
async def mark_prefab_removed(prefab_id: str, stub: KnitterGrpcStub, metadata):
    request = MarkEntityRemovedRequest(manage_id=PREFABS_MANAGE_ID, entity_id=prefab_id)
    try:
        response = stub.MarkEntityRemoved(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())
