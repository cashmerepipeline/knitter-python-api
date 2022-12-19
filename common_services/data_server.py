import grpc

async def get_data_server_configs(request, stub, metadata):
    try:
        response = stub.GetDataServerConfigs(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

async def new_data(request, stub, metadata):
    try:
        response = stub.NewData(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

async def list_data(request, stub, metadata):
    try:
        response = stub.ListData(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

async def list_data_stages(request, stub, metadata):
    try:
        response = stub.ListDataStages(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

async def add_data_stage_version(request, stub, metadata):
    try:
        response = stub.AddDataStageVersion(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

async def mark_data_removed(request, stub, metadata):
    try:
        response = stub.MarkDataRemoved(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

async def file_data_upload_file(request, stub, metadata):
    try:
        response = stub.FileDataUploadFile(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

async def file_data_download_file(request, stub, metadata):
    try:
        response = stub.FileDataDownloadFile(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)
    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())

