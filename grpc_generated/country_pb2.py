# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: country.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import name_pb2 as name__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rcountry.proto\x12\x08\x63\x61shmere\x1a\nname.proto\"{\n\x11NewCountryRequest\x12\x1c\n\x04name\x18\x01 \x01(\x0b\x32\x0e.cashmere.Name\x12\x0e\n\x06native\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\t\x12\x17\n\x0fphone_area_code\x18\x04 \x01(\t\x12\x11\n\tlanguages\x18\x05 \x03(\t\"$\n\x12NewCountryResponse\x12\x0e\n\x06result\x18\x01 \x01(\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'country_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _NEWCOUNTRYREQUEST._serialized_start=39
  _NEWCOUNTRYREQUEST._serialized_end=162
  _NEWCOUNTRYRESPONSE._serialized_start=164
  _NEWCOUNTRYRESPONSE._serialized_end=200
# @@protoc_insertion_point(module_scope)
