import grpc

from grpc_generated.knitter_pb2_grpc import KnitterGrpcStub
from entity_pb2 import MarkEntityRemovedRequest

async def add_references(request, stub: KnitterGrpcStub, metadata):
    try:
        response = stub.AddReferences(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

async def remove_referencnes(request, stub: KnitterGrpcStub, metadata):
    try:
        response = stub.RemoveReferences(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

async def list_referencese(request, stub: KnitterGrpcStub, metadata):
    try:
        response = stub.ListReferences(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

async def change_referencne(request, stub: KnitterGrpcStub, metadata):
    try:
        response = stub.ChangeReference(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

