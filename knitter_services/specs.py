import grpc
from grpc_generated.knitter_pb2_grpc import KnitterGrpcStub
from entity_pb2 import MarkEntityRemovedRequest

async def new_specs(request, stub: KnitterGrpcStub, metadata):
    try:
        response = stub.NewSpecs(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

async def list_specs(request, stub: KnitterGrpcStub, metadata):
    try:
        response = stub.ListSpecs(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

async def list_specs_prefabs(request, stub: KnitterGrpcStub, metadata):
    try:
        response = stub.ListSpecsPrefabs(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())
