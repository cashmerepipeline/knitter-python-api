import grpc

async def new_language_code(request, stub, metadata):
    try:
        response = stub.NewLanguageCode(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

async def edit_language_code(request, stub, metadata):
    try:
        response = stub.EditLanguageCode(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

