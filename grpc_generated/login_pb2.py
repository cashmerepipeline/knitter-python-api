# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: login.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import account_status_pb2 as account__status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0blogin.proto\x12\x0f\x61\x63\x63ount_service\x1a\x14\x61\x63\x63ount_status.proto\"B\n\x0cLoginRequest\x12\x11\n\tarea_code\x18\x01 \x01(\t\x12\r\n\x05phone\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\".\n\rLoginResponse\x12\x0e\n\x06person\x18\x01 \x01(\x0c\x12\r\n\x05token\x18\x02 \x01(\t\"\x0f\n\rLogoutRequest\">\n\x0eLogoutResponse\x12,\n\x06result\x18\x01 \x01(\x0e\x32\x1c.account_service.LoginStatus\">\n\x19LoginWithValidCodeRequest\x12\r\n\x05phone\x18\x01 \x01(\t\x12\x12\n\nvalid_code\x18\x02 \x01(\t\",\n\x1aLoginWithValidCodeResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\"\'\n\x16GetValidateCodeRequest\x12\r\n\x05phone\x18\x01 \x01(\t\")\n\x17GetValidateCodeResponse\x12\x0e\n\x06result\x18\x01 \x01(\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'login_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LOGINREQUEST._serialized_start=54
  _LOGINREQUEST._serialized_end=120
  _LOGINRESPONSE._serialized_start=122
  _LOGINRESPONSE._serialized_end=168
  _LOGOUTREQUEST._serialized_start=170
  _LOGOUTREQUEST._serialized_end=185
  _LOGOUTRESPONSE._serialized_start=187
  _LOGOUTRESPONSE._serialized_end=249
  _LOGINWITHVALIDCODEREQUEST._serialized_start=251
  _LOGINWITHVALIDCODEREQUEST._serialized_end=313
  _LOGINWITHVALIDCODERESPONSE._serialized_start=315
  _LOGINWITHVALIDCODERESPONSE._serialized_end=359
  _GETVALIDATECODEREQUEST._serialized_start=361
  _GETVALIDATECODEREQUEST._serialized_end=400
  _GETVALIDATECODERESPONSE._serialized_start=402
  _GETVALIDATECODERESPONSE._serialized_end=443
# @@protoc_insertion_point(module_scope)
