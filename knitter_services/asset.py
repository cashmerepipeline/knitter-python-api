import grpc

from grpc_generated.knitter_pb2_grpc import KnitterGrpcStub


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

async def get_asset_prefabs(request, stub:KnitterGrpcStub, metadata):
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
