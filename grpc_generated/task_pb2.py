# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: task.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import name_pb2 as name__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ntask.proto\x12\x08\x63\x61shmere\x1a\nname.proto\"D\n\x0eNewTaskRequest\x12\x14\n\x0cwork_node_id\x18\x01 \x01(\t\x12\x1c\n\x04name\x18\x02 \x01(\x0b\x32\x0e.cashmere.Name\"!\n\x0fNewTaskResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\"H\n\x12NewTaskDataRequest\x12\x0f\n\x07task_id\x18\x01 \x01(\t\x12!\n\tdata_name\x18\x02 \x01(\x0b\x32\x0e.cashmere.Name\"%\n\x13NewTaskDataResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\">\n\x1a\x41ssociateDataToTaskRequest\x12\x0f\n\x07\x64\x61ta_id\x18\x01 \x01(\t\x12\x0f\n\x07task_id\x18\x02 \x01(\t\"-\n\x1b\x41ssociateDataToTaskResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\"$\n\x11\x43ommitTaskRequest\x12\x0f\n\x07task_id\x18\x01 \x01(\t\"$\n\x12\x43ommitTaskResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\"U\n\x15MarkTaskStatusRequest\x12\x0f\n\x07task_id\x18\x01 \x01(\t\x12\x15\n\rstatus_set_id\x18\x02 \x01(\t\x12\x14\n\x0cstatus_index\x18\x03 \x01(\x05\"(\n\x16MarkTaskStatusResponse\x12\x0e\n\x06result\x18\x01 \x01(\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'task_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _NEWTASKREQUEST._serialized_start=36
  _NEWTASKREQUEST._serialized_end=104
  _NEWTASKRESPONSE._serialized_start=106
  _NEWTASKRESPONSE._serialized_end=139
  _NEWTASKDATAREQUEST._serialized_start=141
  _NEWTASKDATAREQUEST._serialized_end=213
  _NEWTASKDATARESPONSE._serialized_start=215
  _NEWTASKDATARESPONSE._serialized_end=252
  _ASSOCIATEDATATOTASKREQUEST._serialized_start=254
  _ASSOCIATEDATATOTASKREQUEST._serialized_end=316
  _ASSOCIATEDATATOTASKRESPONSE._serialized_start=318
  _ASSOCIATEDATATOTASKRESPONSE._serialized_end=363
  _COMMITTASKREQUEST._serialized_start=365
  _COMMITTASKREQUEST._serialized_end=401
  _COMMITTASKRESPONSE._serialized_start=403
  _COMMITTASKRESPONSE._serialized_end=439
  _MARKTASKSTATUSREQUEST._serialized_start=441
  _MARKTASKSTATUSREQUEST._serialized_end=526
  _MARKTASKSTATUSRESPONSE._serialized_start=528
  _MARKTASKSTATUSRESPONSE._serialized_end=568
# @@protoc_insertion_point(module_scope)
