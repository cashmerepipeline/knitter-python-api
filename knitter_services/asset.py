import grpc

from grpc_generated.knitter_pb2_grpc import KnitterGrpcStub
from id_codes.manage_ids import ASSETS_MANAGE_ID
from entity_pb2 import MarkEntityRemovedRequest


async def new_asset(request, stub:KnitterGrpcStub, metadata):
    try:
        response = stub.NewAsset(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

async def get_asset_specses(request, stub:KnitterGrpcStub, metadata):
    try:
        response = stub.GetAssetSpecses(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

async def get_asset_specs_prefabs(request, stub:KnitterGrpcStub, metadata):
    try:
        response = stub.GetAssetPrefabs(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

async def mark_asset_satus(request, stub:KnitterGrpcStub, metadata):
    try:
        response = stub.MarkAssetStatus(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

async def get_referenced_assets(request, stub:KnitterGrpcStub, metadata):
    try:
        response = stub.GetReferencedAssets(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

# 标记移除
async def mark_asset_removed(asset_id: str, stub: KnitterGrpcStub, metadata):
    request = MarkEntityRemovedRequest(manage_id=ASSETS_MANAGE_ID, entity_id=asset_id)
    try:
        response = stub.MarkEntityRemoved(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())
