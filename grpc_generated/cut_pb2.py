# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cut.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import name_pb2 as name__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tcut.proto\x12\nio.knitter\x1a\nname.proto\"W\n\rNewCutRequest\x12\x13\n\x0bsequence_id\x18\x01 \x01(\t\x12\x1c\n\x04name\x18\x02 \x01(\x0b\x32\x0e.cashmere.Name\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\" \n\x0eNewCutResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\">\n\x19\x43utReferenceAssetsRequest\x12\x0e\n\x06\x63ut_id\x18\x01 \x01(\t\x12\x11\n\tasset_ids\x18\x02 \x03(\t\",\n\x1a\x43utReferenceAssetsResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\"(\n\x16\x43utRefereceSetsRequest\x12\x0e\n\x06\x63ut_id\x18\x01 \x01(\t\")\n\x17\x43utRefereceSetsResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\"&\n\x14MarkCutStatusRequest\x12\x0e\n\x06\x63ut_id\x18\x01 \x01(\t\"\'\n\x15MarkCutStatusResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\"/\n\x1dGetCutReferencedAssetsRequest\x12\x0e\n\x06\x63ut_id\x18\x01 \x01(\t\"0\n\x1eGetCutReferencedAssetsResponse\x12\x0e\n\x06\x61ssets\x18\x01 \x03(\x0c\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cut_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _NEWCUTREQUEST._serialized_start=37
  _NEWCUTREQUEST._serialized_end=124
  _NEWCUTRESPONSE._serialized_start=126
  _NEWCUTRESPONSE._serialized_end=158
  _CUTREFERENCEASSETSREQUEST._serialized_start=160
  _CUTREFERENCEASSETSREQUEST._serialized_end=222
  _CUTREFERENCEASSETSRESPONSE._serialized_start=224
  _CUTREFERENCEASSETSRESPONSE._serialized_end=268
  _CUTREFERECESETSREQUEST._serialized_start=270
  _CUTREFERECESETSREQUEST._serialized_end=310
  _CUTREFERECESETSRESPONSE._serialized_start=312
  _CUTREFERECESETSRESPONSE._serialized_end=353
  _MARKCUTSTATUSREQUEST._serialized_start=355
  _MARKCUTSTATUSREQUEST._serialized_end=393
  _MARKCUTSTATUSRESPONSE._serialized_start=395
  _MARKCUTSTATUSRESPONSE._serialized_end=434
  _GETCUTREFERENCEDASSETSREQUEST._serialized_start=436
  _GETCUTREFERENCEDASSETSREQUEST._serialized_end=483
  _GETCUTREFERENCEDASSETSRESPONSE._serialized_start=485
  _GETCUTREFERENCEDASSETSRESPONSE._serialized_end=533
# @@protoc_insertion_point(module_scope)
