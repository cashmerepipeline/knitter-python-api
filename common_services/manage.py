#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
Project: cashmere_python_client
Creator: 闫刚
Create time: 2020-10-27 11:09
Introduction:
"""

import grpc
import manage_pb2


async def new_manage(id: int, name, schema, stub, metadata):
    """ """
    request = manage_pb2.NewManageRequest(id=id, name=name, schema=schema)
    try:
        response = stub.NewManage.with_call(request, metadata=metadata)

        return (grpc.StatusCode.OK, response, None)

    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())


async def get_manages(request: manage_pb2.GetManagesRequest, stub, metadata):
    try:
        response = stub.GetManages(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)

    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())


async def get_manage_entry_count(request, stub, metadata):
    try:
        response = stub.GetManageEntryCount(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)

    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())


async def get_manage_schema(request, stub, metadata):
    try:
        response = stub.GetManageSchema(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)

    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())


async def new_manage_schema_field(manage_id, field, stub, metadata):
    request = manage_pb2.NewSchemaFieldRequest(manage_id=manage_id, field=field)
    try:
        response, call = stub.NewSchemaField.with_call(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)

    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())


async def edit_manage_schema_field_name(
    manage_id, field_id, local, new_name, stub, metadata
):
    request = manage_pb2.EditSchemaFieldNameRequest(
        manage_id=manage_id, field_id=field_id, local=local, new_name=new_name
    )
    try:
        response, call = stub.EditSchemaFieldName.with_call(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)

    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())


async def mark_manage_schema_field_removed(request, stub, metadata):
    try:
        response, _call = stub.MarkSchemaFieldRemoved.with_call(request, metadata=metadata)
        return (grpc.StatusCode.OK, response, None)

    except grpc.RpcError as e:
        # print(e.code(), None, e.details())
        return (e.code(), None, e.details())
