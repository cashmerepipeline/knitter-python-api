import grpc

from grpc_generated.knitter_pb2_grpc import KnitterGrpcStub
from id_codes.manage_ids import ASSET_COLLECTIONS_MANAGE_ID
from entity_pb2 import GetEntitiesPageRequest


async def new_asset_collection(request, stub: KnitterGrpcStub, metadata):
    try:
        response = stub.NewAssetCollection(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())


async def get_asset_collection_assets_page(request, stub: KnitterGrpcStub, metadata):
    try:
        response = stub.GetAssetCollectionAssetsPage(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())


async def get_asset_collection_assemblies_page(
    request, stub: KnitterGrpcStub, metadata
):
    try:
        response = stub.GetAssetCollectionAssembliesPage(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())


# 取得资产集列表, 便捷工具函数
async def list_asset_collections(
    page_index, conditions, stub: KnitterGrpcStub, metadata
):
    request = GetEntitiesPageRequest(
        manage_id=ASSET_COLLECTIONS_MANAGE_ID,
        page_index=page_index,
        conditions=conditions,
    )

    try:
        response = stub.GetEntitiesPage(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())


# 标记资产集状态
async def mark_asset_collection_status(request, stub: KnitterGrpcStub, metadata):
    try:
        response = stub.MarkAssetCollectionStatus(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())


# 标记移除
async def mark_asset_collection_removed(
    asset_collection_id: str, stub: KnitterGrpcStub, metadata
):
    request = MarkEntityRemovedRequest(
        manage_id=ASSET_COLLECTIONS_MANAGE_ID, entity_id=asset_collection_id
    )
    try:
        response = stub.MarkEntityRemoved(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())
