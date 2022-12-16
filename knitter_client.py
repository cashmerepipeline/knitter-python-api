from grpc import Channel
from knitter_pb2_grpc import KnitterGrpcStub;

def get_client_stub(channel: Channel):
    stub = KnitterGrpcStub(channel=channel)
    return stub
