import grpc


area_code = "86"
phone = "10000000000"
passwd = "root"
# passwd = "123456"
group = "10000"

server = "127.0.0.1:8800"
insecure_channel = grpc.insecure_channel(server);
