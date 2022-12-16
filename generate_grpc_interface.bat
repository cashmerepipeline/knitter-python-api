python -m grpc_tools.protoc -I../cashmere_core/protocols -I../cashmere_core/account_server/protocols --python_out=./grpc_generated/ --grpc_python_out=./grpc_generated  ../cashmere_core/account_server/protocols/account_service.proto

python -m grpc_tools.protoc -I../cashmere_core/protocols -I../cashmere_core/account_server/protocols --python_out=./grpc_generated/  ../cashmere_core/account_server/protocols/account.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols -I../cashmere_core/account_server/protocols --python_out=./grpc_generated/  ../cashmere_core/account_server/protocols/login.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols -I../cashmere_core/account_server/protocols --python_out=./grpc_generated/  ../cashmere_core/account_server/protocols/status.proto

python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/answer.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/area.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/cashmere.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/color.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/comment.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/country.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/data.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/data_server.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/data_stage.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/entity.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/entity_template.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/event.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/file_data.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/file_info.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/gender.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/group.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/language_code.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/manage.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/manage_schema.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/name.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/person.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/phase.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/phone_area_code.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/position.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/procedure.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/property_type.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/question.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/range.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/readme.md
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/results.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/season.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/sequence_data.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/set_data.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/set_data_info.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/tag.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/tag_map.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/tag_type.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/task.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/use_clothes.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/view.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/work.proto
python -m grpc_tools.protoc -I../cashmere_core/protocols --python_out=./grpc_generated/   ../cashmere_core/protocols/work_node.proto


python -m grpc_tools.protoc -I../knitter/protocols -I../cashmere_core/protocols --python_out=./grpc_generated/ --grpc_python_out=./grpc_generated  ../knitter/protocols/knitter.proto

python -m grpc_tools.protoc -I../knitter/protocols -I../cashmere_core/protocols --python_out=./grpc_generated/  ../knitter/protocols/assembly.proto
python -m grpc_tools.protoc -I../knitter/protocols -I../cashmere_core/protocols --python_out=./grpc_generated/  ../knitter/protocols/asset.proto
python -m grpc_tools.protoc -I../knitter/protocols -I../cashmere_core/protocols --python_out=./grpc_generated/  ../knitter/protocols/asset_collection.proto
python -m grpc_tools.protoc -I../knitter/protocols -I../cashmere_core/protocols --python_out=./grpc_generated/  ../knitter/protocols/cut.proto
python -m grpc_tools.protoc -I../knitter/protocols -I../cashmere_core/protocols --python_out=./grpc_generated/  ../knitter/protocols/epic.proto
python -m grpc_tools.protoc -I../knitter/protocols -I../cashmere_core/protocols --python_out=./grpc_generated/  ../knitter/protocols/knitter.proto
python -m grpc_tools.protoc -I../knitter/protocols -I../cashmere_core/protocols --python_out=./grpc_generated/  ../knitter/protocols/prefab.proto
python -m grpc_tools.protoc -I../knitter/protocols -I../cashmere_core/protocols --python_out=./grpc_generated/  ../knitter/protocols/project.proto
python -m grpc_tools.protoc -I../knitter/protocols -I../cashmere_core/protocols --python_out=./grpc_generated/  ../knitter/protocols/reference.proto
python -m grpc_tools.protoc -I../knitter/protocols -I../cashmere_core/protocols --python_out=./grpc_generated/  ../knitter/protocols/sequence.proto
python -m grpc_tools.protoc -I../knitter/protocols -I../cashmere_core/protocols --python_out=./grpc_generated/  ../knitter/protocols/set.proto
python -m grpc_tools.protoc -I../knitter/protocols -I../cashmere_core/protocols --python_out=./grpc_generated/  ../knitter/protocols/set_collection.proto
python -m grpc_tools.protoc -I../knitter/protocols -I../cashmere_core/protocols --python_out=./grpc_generated/  ../knitter/protocols/specs.proto
python -m grpc_tools.protoc -I../knitter/protocols -I../cashmere_core/protocols --python_out=./grpc_generated/  ../knitter/protocols/project.proto
python -m grpc_tools.protoc -I../knitter/protocols -I../cashmere_core/protocols --python_out=./grpc_generated/  ../knitter/protocols/library.proto
