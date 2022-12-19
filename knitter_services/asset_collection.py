import grpc

from grpc_generated.knitter_pb2_grpc import KnitterGrpcStub

async def new_asset_collection(request, stub: KnitterGrpcStub, metadata):
    try:
        response = stub.NewAssetCollection(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

async def get_asset_collection_associated_assets_page(request, stub: KnitterGrpcStub, metadata):
    try:
        response = stub.GetAssetCollectionAssociatedAssetsPage(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

async def get_asset_collection_associated_assemblies_page(request, stub: KnitterGrpcStub, metadata):
    try:
        response = stub.GetAssetCollectionAssociatedAssembliesPage(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

