# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: specs.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import name_pb2 as name__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bspecs.proto\x12\nio.knitter\x1a\nname.proto\"v\n\x0fNewSpecsRequest\x12\x17\n\x0fowner_manage_id\x18\x01 \x01(\x05\x12\x17\n\x0fowner_entity_id\x18\x02 \x01(\t\x12\x1c\n\x04name\x18\x03 \x01(\x0b\x32\x0e.cashmere.Name\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\"\"\n\x10NewSpecsResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\"D\n\x10ListSpecsRequest\x12\x17\n\x0fowner_manage_id\x18\x01 \x01(\x05\x12\x17\n\x0fowner_entity_id\x18\x02 \x01(\t\"$\n\x11ListSpecsResponse\x12\x0f\n\x07specses\x18\x01 \x03(\x0c\"+\n\x17ListSpecsPrefabsRequest\x12\x10\n\x08specs_id\x18\x01 \x01(\t\"+\n\x18ListSpecsPrefabsResponse\x12\x0f\n\x07prefabs\x18\x01 \x03(\x0c\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'specs_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _NEWSPECSREQUEST._serialized_start=39
  _NEWSPECSREQUEST._serialized_end=157
  _NEWSPECSRESPONSE._serialized_start=159
  _NEWSPECSRESPONSE._serialized_end=193
  _LISTSPECSREQUEST._serialized_start=195
  _LISTSPECSREQUEST._serialized_end=263
  _LISTSPECSRESPONSE._serialized_start=265
  _LISTSPECSRESPONSE._serialized_end=301
  _LISTSPECSPREFABSREQUEST._serialized_start=303
  _LISTSPECSPREFABSREQUEST._serialized_end=346
  _LISTSPECSPREFABSRESPONSE._serialized_start=348
  _LISTSPECSPREFABSRESPONSE._serialized_end=391
# @@protoc_insertion_point(module_scope)
