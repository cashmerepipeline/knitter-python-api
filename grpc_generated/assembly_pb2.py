# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: assembly.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import name_pb2 as name__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0e\x61ssembly.proto\x12\nio.knitter\x1a\nname.proto\"d\n\x12NewAssemblyRequest\x12\x1b\n\x13\x61sset_collection_id\x18\x01 \x01(\t\x12\x1c\n\x04name\x18\x02 \x01(\x0b\x32\x0e.cashmere.Name\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\"%\n\x13NewAssemblyResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\"?\n\x15UpdateAssemblyRequest\x12\x13\n\x0b\x61ssembly_id\x18\x01 \x01(\t\x12\x11\n\tasset_ids\x18\x02 \x03(\t\"(\n\x16UpdateAssemblyResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\"t\n\x1aReferenceAssembliesRequest\x12\x11\n\tmanage_id\x18\x01 \x01(\x05\x12\x11\n\tentity_id\x18\x02 \x01(\t\x12\x1a\n\x12reference_field_id\x18\x03 \x01(\t\x12\x14\n\x0c\x61ssembly_ids\x18\x04 \x03(\t\"-\n\x1bReferenceAssembliesResponse\x12\x0e\n\x06result\x18\x01 \x01(\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'assembly_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _NEWASSEMBLYREQUEST._serialized_start=42
  _NEWASSEMBLYREQUEST._serialized_end=142
  _NEWASSEMBLYRESPONSE._serialized_start=144
  _NEWASSEMBLYRESPONSE._serialized_end=181
  _UPDATEASSEMBLYREQUEST._serialized_start=183
  _UPDATEASSEMBLYREQUEST._serialized_end=246
  _UPDATEASSEMBLYRESPONSE._serialized_start=248
  _UPDATEASSEMBLYRESPONSE._serialized_end=288
  _REFERENCEASSEMBLIESREQUEST._serialized_start=290
  _REFERENCEASSEMBLIESREQUEST._serialized_end=406
  _REFERENCEASSEMBLIESRESPONSE._serialized_start=408
  _REFERENCEASSEMBLIESRESPONSE._serialized_end=453
# @@protoc_insertion_point(module_scope)
