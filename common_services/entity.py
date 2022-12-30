import grpc

# 实体，主要是实体查询
async def get_entity(request, stub, metadata):
    try:
        response = stub.GetEntity(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

async def get_entities(request, stub, metadata):
    try:
        response = stub.GetEntities(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

async def get_entities_page(request, stub, metadata):
    try:
        response = stub.GetEntitiesPage(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())
                                    
# 编辑实体属性，非数据结构
async def edit_entity_field(request, stub, metadata):
    try:
        response = stub.EditEntityField(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

# 编辑实体属性，MAP数据结构
async def edit_entity_map_field(request, stub, metadata):
    try:
        response = stub.EditEntityMapField(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

async def edit_entity_map_field_remove_key(request, stub, metadata):
    try:
        response = stub.EditEntityMapFieldRemoveKey(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

# 编辑实体属性，List数据结构
async def edit_entity_array_field_add_items(request, stub, metadata):
    try:
        response = stub.EditEntityArrayFieldAddItems(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

async def edit_entity_array_field_remove_items(request, stub, metadata):
    try:
        response = stub.EditEntityArrayFieldRemoveItems(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())
