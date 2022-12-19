import grpc

from grpc_generated.knitter_pb2_grpc import KnitterGrpcStub
async def new_cut(request, stub: KnitterGrpcStub, metadata):
    try:
        response = stub.NewCut(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())
async def get_cut_referenced_assets(request, stub: KnitterGrpcStub, metadata):
    try:
        response = stub.GetCutReferencedAssets(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())
async def mark_cut_status(request, stub: KnitterGrpcStub, metadata):
    try:
        response = stub.MarkCutStatus(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())
