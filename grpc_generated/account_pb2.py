# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: account.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import name_pb2 as name__pb2
import account_status_pb2 as account__status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\raccount.proto\x12\x0f\x61\x63\x63ount_service\x1a\nname.proto\x1a\x14\x61\x63\x63ount_status.proto\"j\n\x11NewAccountRequest\x12\x11\n\tarea_code\x18\x01 \x01(\t\x12\r\n\x05phone\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\x12!\n\tnick_name\x18\x04 \x01(\x0b\x32\x0e.cashmere.Name\"$\n\x12NewAccountResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\"b\n\x0fRegisterRequest\x12\x17\n\x0forganization_id\x18\x01 \x01(\t\x12\x15\n\rdepartment_id\x18\x02 \x01(\t\x12\r\n\x05phone\x18\x04 \x01(\t\x12\x10\n\x08password\x18\x05 \x01(\t\"\"\n\x10RegisterResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\"O\n\x15\x43hangeOwnPhoneRequest\x12\x11\n\told_phone\x18\x01 \x01(\t\x12\x11\n\tnew_phone\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\"(\n\x16\x43hangePhoneOwnResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\"B\n\x1a\x41\x64\x64\x41\x63\x63ountIntoGroupRequest\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12\x10\n\x08group_id\x18\x02 \x01(\t\"-\n\x1b\x41\x64\x64\x41\x63\x63ountIntoGroupResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\"E\n\x1dRemoveAccountFromGroupRequest\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12\x10\n\x08group_id\x18\x02 \x01(\t\"0\n\x1eRemoveAccountFromGroupResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\"`\n\x1a\x43hangeAccountStatusRequest\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12.\n\x06status\x18\x02 \x01(\x0e\x32\x1e.account_service.AccountStatus\"M\n\x1b\x43hangeAccountStatusResponse\x12.\n\x06result\x18\x01 \x01(\x0e\x32\x1e.account_service.AccountStatusb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'account_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _NEWACCOUNTREQUEST._serialized_start=68
  _NEWACCOUNTREQUEST._serialized_end=174
  _NEWACCOUNTRESPONSE._serialized_start=176
  _NEWACCOUNTRESPONSE._serialized_end=212
  _REGISTERREQUEST._serialized_start=214
  _REGISTERREQUEST._serialized_end=312
  _REGISTERRESPONSE._serialized_start=314
  _REGISTERRESPONSE._serialized_end=348
  _CHANGEOWNPHONEREQUEST._serialized_start=350
  _CHANGEOWNPHONEREQUEST._serialized_end=429
  _CHANGEPHONEOWNRESPONSE._serialized_start=431
  _CHANGEPHONEOWNRESPONSE._serialized_end=471
  _ADDACCOUNTINTOGROUPREQUEST._serialized_start=473
  _ADDACCOUNTINTOGROUPREQUEST._serialized_end=539
  _ADDACCOUNTINTOGROUPRESPONSE._serialized_start=541
  _ADDACCOUNTINTOGROUPRESPONSE._serialized_end=586
  _REMOVEACCOUNTFROMGROUPREQUEST._serialized_start=588
  _REMOVEACCOUNTFROMGROUPREQUEST._serialized_end=657
  _REMOVEACCOUNTFROMGROUPRESPONSE._serialized_start=659
  _REMOVEACCOUNTFROMGROUPRESPONSE._serialized_end=707
  _CHANGEACCOUNTSTATUSREQUEST._serialized_start=709
  _CHANGEACCOUNTSTATUSREQUEST._serialized_end=805
  _CHANGEACCOUNTSTATUSRESPONSE._serialized_start=807
  _CHANGEACCOUNTSTATUSRESPONSE._serialized_end=884
# @@protoc_insertion_point(module_scope)
