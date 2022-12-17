# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: manage_schema.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import entity_pb2 as entity__pb2
import view_pb2 as view__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13manage_schema.proto\x12\x08\x63\x61shmere\x1a\x0c\x65ntity.proto\x1a\nview.proto\"O\n\x0bSchemaField\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08name_map\x18\x02 \x01(\x0c\x12\x11\n\tdata_type\x18\x03 \x01(\t\x12\x0f\n\x07removed\x18\x04 \x01(\x08\"+\n\x16GetManageSchemaRequest\x12\x11\n\tmanage_id\x18\x01 \x01(\x05\"@\n\x17GetManageSchemaResponse\x12%\n\x06\x66ields\x18\x01 \x03(\x0b\x32\x15.cashmere.SchemaField\"P\n\x15NewSchemaFieldRequest\x12\x11\n\tmanage_id\x18\x01 \x01(\x05\x12$\n\x05\x66ield\x18\x02 \x01(\x0b\x32\x15.cashmere.SchemaField\"(\n\x16NewSchemaFieldResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\"D\n\x1dMarkSchemaFieldRemovedRequest\x12\x11\n\tmanage_id\x18\x01 \x01(\x05\x12\x10\n\x08\x66ield_id\x18\x02 \x01(\x05\"0\n\x1eMarkSchemaFieldRemovedResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\"e\n\x1a\x45\x64itSchemaFieldNameRequest\x12\x11\n\tmanage_id\x18\x01 \x01(\x05\x12\x10\n\x08\x66ield_id\x18\x02 \x01(\x05\x12\x10\n\x08language\x18\x03 \x01(\t\x12\x10\n\x08new_name\x18\x04 \x01(\t\"-\n\x1b\x45\x64itSchemaFieldNameResponse\x12\x0e\n\x06result\x18\x01 \x01(\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'manage_schema_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SCHEMAFIELD._serialized_start=59
  _SCHEMAFIELD._serialized_end=138
  _GETMANAGESCHEMAREQUEST._serialized_start=140
  _GETMANAGESCHEMAREQUEST._serialized_end=183
  _GETMANAGESCHEMARESPONSE._serialized_start=185
  _GETMANAGESCHEMARESPONSE._serialized_end=249
  _NEWSCHEMAFIELDREQUEST._serialized_start=251
  _NEWSCHEMAFIELDREQUEST._serialized_end=331
  _NEWSCHEMAFIELDRESPONSE._serialized_start=333
  _NEWSCHEMAFIELDRESPONSE._serialized_end=373
  _MARKSCHEMAFIELDREMOVEDREQUEST._serialized_start=375
  _MARKSCHEMAFIELDREMOVEDREQUEST._serialized_end=443
  _MARKSCHEMAFIELDREMOVEDRESPONSE._serialized_start=445
  _MARKSCHEMAFIELDREMOVEDRESPONSE._serialized_end=493
  _EDITSCHEMAFIELDNAMEREQUEST._serialized_start=495
  _EDITSCHEMAFIELDNAMEREQUEST._serialized_end=596
  _EDITSCHEMAFIELDNAMERESPONSE._serialized_start=598
  _EDITSCHEMAFIELDNAMERESPONSE._serialized_end=643
# @@protoc_insertion_point(module_scope)
