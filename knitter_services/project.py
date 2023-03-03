import grpc

from grpc_generated.knitter_pb2_grpc import KnitterGrpcStub
from entity_pb2 import MarkEntityRemovedRequest

async def new_project(request, stub: KnitterGrpcStub, metadata):
    try:
        response = stub.NewProject(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

async def associate_asset_collections_to_project(request, stub: KnitterGrpcStub, metadata):
    try:
        response = stub.AssociateAssetCollectionsToProject(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

async def associate_set_collections_to_project(request, stub: KnitterGrpcStub, metadata):
    try:
        response = stub.AssociateSetCollectionsToProject(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())
async def get_project_associated_asset_collections(request, stub: KnitterGrpcStub, metadata):
    try:
        response = stub.GetProjectAssociatedAssetCollections(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

async def get_project_associated_set_collections(request, stub: KnitterGrpcStub, metadata):
    try:
        response = stub.GetProjectAssociatedSetCollections(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

async def change_project_status(request, stub: KnitterGrpcStub, metadata):
    try:
        response = stub.ChangeProjectStatus(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())
