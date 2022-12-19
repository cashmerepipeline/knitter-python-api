import grpc

async def new_country(request, stub, metadata):
    try:
        response = stub.NewCountry(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

