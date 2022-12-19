import grpc

async def change_manage_read_rule(request, stub, metadata):
    try:
        response = stub.ChangeManageReadRule(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)

    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

async def change_manage_write_rule(request, stub, metadata):
    try:
        response = stub.ChangeManageWriteRule(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)

    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

async def change_collection_read_rule(request, stub, metadata):
    try:
        response = stub.ChangeCollectionReadRule(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)

    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

async def change_collection_write_rule(request, stub, metadata):
    try:
        response = stub.ChangeCollectionWriteRule(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)

    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

async def change_field_read_rule(request, stub, metadata):
    try:
        response = stub.ChangeFieldReadRule(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)

    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

async def change_field_write_rule(request, stub, metadata):
    try:
        response = stub.ChangeFieldWriteRule(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)

    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())
