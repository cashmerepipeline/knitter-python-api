import grpc
import bson

from grpc_generated.knitter_pb2_grpc import KnitterGrpcStub
from entity_pb2 import EditEntityArrayFieldRemoveItemsRequest
from id_codes.manage_ids import PROJECTS_MANAGE_ID
from id_codes.field_ids import PROJECTS_ASSOCIATED_SET_COLLECTIONS_FIELD_ID

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

async def deassociate_asset_collections_from_project(request, stub: KnitterGrpcStub, metadata):
    try:
        response = stub.DeassociateAssetCollectionsFromProject(request, metadata=metadata)
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

async def deassociate_set_collections_from_project(request, stub: KnitterGrpcStub, metadata):
    try:
        response = stub.DeassociateSetCollectionsFromProject(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

async def _deassociate_set_collections_from_project(project_id, collection_ids:list, stub:KnitterGrpcStub, metadata):
    new_value = dict({str(PROJECTS_ASSOCIATED_SET_COLLECTIONS_FIELD_ID): collection_ids})
    request = EditEntityArrayFieldRemoveItemsRequest(
        manage_id=PROJECTS_MANAGE_ID,
        entity_id=project_id,
        field_id=str(PROJECTS_ASSOCIATED_SET_COLLECTIONS_FIELD_ID),
        items=bson.encode(document=new_value)
    )

    try:
        response = stub.EditEntityArrayFieldRemoveItems(request, metadata=metadata) 
        return (grpc.StatusCode.OK, response, None) 
    except grpc.RpcError as e: 
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
