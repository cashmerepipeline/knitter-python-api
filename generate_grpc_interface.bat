python -m grpc_tools.protoc -I../cashmere_core/protocols -I../cashmere_core/account_server/protocols --python_out=./grpc_generated/ --grpc_python_out=./grpc_generated  ../cashmere_core/account_server/protocols/account_service.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols -I../cashmere_core/account_server/protocols --python_out=./grpc_generated/  ../cashmere_core/account_server/protocols/account.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols -I../cashmere_core/account_server/protocols --python_out=./grpc_generated/  ../cashmere_core/account_server/protocols/login.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols -I../cashmere_core/account_server/protocols --python_out=./grpc_generated/  ../cashmere_core/account_server/protocols/status.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/manage.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/tag.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/comment.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/question.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/answer.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/name.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/area.proto