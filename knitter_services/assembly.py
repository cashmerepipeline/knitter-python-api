import grpc

from grpc_generated.knitter_pb2_grpc import KnitterGrpcStub
async def new_assembly(request, stub: KnitterGrpcStub, metadata):
    try:
        response = stub.NewAssembly(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())
