# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: language_code.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import name_pb2 as name__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13language_code.proto\x12\x08\x63\x61shmere\x1a\nname.proto\".\n\x0cLanguageCode\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x10\n\x08name_map\x18\x02 \x01(\x0c\"Y\n\x16NewLanguageCodeRequest\x12\x1c\n\x04name\x18\x01 \x01(\x0b\x32\x0e.cashmere.Name\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x13\n\x0bnative_name\x18\x03 \x01(\t\")\n\x17NewLanguageCodeResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\"K\n\x17\x45\x64itLanguageCodeRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08new_code\x18\x02 \x01(\t\x12\x12\n\nnew_native\x18\x03 \x01(\t\"*\n\x18\x45\x64itLanguageCodeResponse\x12\x0e\n\x06result\x18\x01 \x01(\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'language_code_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LANGUAGECODE._serialized_start=45
  _LANGUAGECODE._serialized_end=91
  _NEWLANGUAGECODEREQUEST._serialized_start=93
  _NEWLANGUAGECODEREQUEST._serialized_end=182
  _NEWLANGUAGECODERESPONSE._serialized_start=184
  _NEWLANGUAGECODERESPONSE._serialized_end=225
  _EDITLANGUAGECODEREQUEST._serialized_start=227
  _EDITLANGUAGECODEREQUEST._serialized_end=302
  _EDITLANGUAGECODERESPONSE._serialized_start=304
  _EDITLANGUAGECODERESPONSE._serialized_end=346
# @@protoc_insertion_point(module_scope)
