import grpc

from grpc_generated.knitter_pb2_grpc import KnitterGrpcStub

async def new_set_collection(request, stub: KnitterGrpcStub, metadata):
    try:
        response = stub.NewSetCollection(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

async def new_set(request, stub: KnitterGrpcStub, metadata):
    try:
        response = stub.NewSet(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

async def mark_set_satus(request, stub: KnitterGrpcStub, metadata):
    try:
        response = stub.MarkSetSatus(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

