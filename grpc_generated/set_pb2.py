# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: set.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import name_pb2 as name__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tset.proto\x12\nio.knitter\x1a\nname.proto\"]\n\rNewSetRequest\x12\x19\n\x11set_collection_id\x18\x01 \x01(\t\x12\x1c\n\x04name\x18\x02 \x01(\x0b\x32\x0e.cashmere.Name\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\" \n\x0eNewSetResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\"9\n\x15ReferencAssetsRequest\x12\x0e\n\x06set_id\x18\x01 \x01(\t\x12\x10\n\x08\x61sset_id\x18\x02 \x03(\t\"(\n\x16ReferencAssetsResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\"B\n\x1dUpdateReferencedAssetsRequest\x12\x0e\n\x06set_id\x18\x01 \x01(\t\x12\x11\n\tasset_ids\x18\x02 \x03(\t\"0\n\x1eUpdateReferencedAssetsResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\"M\n\x14ReferenceSetsRequest\x12\x11\n\tmanage_id\x18\x01 \x01(\x05\x12\x11\n\tentity_id\x18\x02 \x01(\t\x12\x0f\n\x07set_ids\x18\x03 \x03(\t\"\'\n\x15ReferenceSetsResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\"&\n\x14MarkSetStatusRequest\x12\x0e\n\x06set_id\x18\x01 \x01(\t\"\'\n\x15MarkSetStatusResponse\x12\x0e\n\x06result\x18\x01 \x01(\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'set_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _NEWSETREQUEST._serialized_start=37
  _NEWSETREQUEST._serialized_end=130
  _NEWSETRESPONSE._serialized_start=132
  _NEWSETRESPONSE._serialized_end=164
  _REFERENCASSETSREQUEST._serialized_start=166
  _REFERENCASSETSREQUEST._serialized_end=223
  _REFERENCASSETSRESPONSE._serialized_start=225
  _REFERENCASSETSRESPONSE._serialized_end=265
  _UPDATEREFERENCEDASSETSREQUEST._serialized_start=267
  _UPDATEREFERENCEDASSETSREQUEST._serialized_end=333
  _UPDATEREFERENCEDASSETSRESPONSE._serialized_start=335
  _UPDATEREFERENCEDASSETSRESPONSE._serialized_end=383
  _REFERENCESETSREQUEST._serialized_start=385
  _REFERENCESETSREQUEST._serialized_end=462
  _REFERENCESETSRESPONSE._serialized_start=464
  _REFERENCESETSRESPONSE._serialized_end=503
  _MARKSETSTATUSREQUEST._serialized_start=505
  _MARKSETSTATUSREQUEST._serialized_end=543
  _MARKSETSTATUSRESPONSE._serialized_start=545
  _MARKSETSTATUSRESPONSE._serialized_end=584
# @@protoc_insertion_point(module_scope)
