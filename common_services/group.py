import grpc

async def new_group(request, stub, metadata):
    try:
        response = stub.NewGroup(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

