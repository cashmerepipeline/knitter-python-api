# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: status.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cstatus.proto\x12\x0f\x61\x63\x63ount_service*<\n\x0bLoginStatus\x12\x0c\n\x08LoggedIn\x10\x00\x12\r\n\tLoggedOut\x10\x01\x12\x10\n\x0cLogginFailed\x10\x02*)\n\rAccountStatus\x12\x0b\n\x07Stopped\x10\x00\x12\x0b\n\x07\x41\x63tived\x10\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'status_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LOGINSTATUS._serialized_start=33
  _LOGINSTATUS._serialized_end=93
  _ACCOUNTSTATUS._serialized_start=95
  _ACCOUNTSTATUS._serialized_end=136
# @@protoc_insertion_point(module_scope)
