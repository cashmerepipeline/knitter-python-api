import grpc

from grpc_generated.knitter_pb2_grpc import KnitterGrpcStub
from entity_pb2 import MarkEntityRemovedRequest

async def new_set_collection(request, stub: KnitterGrpcStub, metadata):
    try:
        response = stub.NewSetCollection(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())
