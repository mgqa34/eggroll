# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: egg.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tegg.proto\x12\x1b\x63om.webank.eggroll.core.egg\"\x1e\n\rCountResponse\x12\r\n\x05value\x18\x01 \x01(\x03\"\x19\n\nGetRequest\x12\x0b\n\x03key\x18\x01 \x01(\x0c\"9\n\x0bGetResponse\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c\x12\x0e\n\x06\x65xists\x18\x03 \x01(\x08\"(\n\nPutRequest\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c\":\n\x0bPutResponse\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c\x12\x0f\n\x07success\x18\x03 \x01(\x08\"\x1e\n\rGetAllRequest\x12\r\n\x05limit\x18\x01 \x01(\x03\"\x1c\n\rDeleteRequest\x12\x0b\n\x03key\x18\x01 \x01(\x0c\".\n\x0e\x44\x65leteResponse\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\x0f\n\x07success\x18\x02 \x01(\x08\"0\n\x1dMapPartitionsWithIndexRequest\x12\x0f\n\x07shuffle\x18\x01 \x01(\x08\"+\n\x0eReduceResponse\x12\n\n\x02id\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\x0c\"&\n\x10\x41ggregateRequest\x12\x12\n\nzero_value\x18\x01 \x01(\x0c\".\n\x11\x41ggregateResponse\x12\n\n\x02id\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\x0c\"/\n\x12WithStoresResponse\x12\n\n\x02id\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\x0c\x62\x06proto3')



_COUNTRESPONSE = DESCRIPTOR.message_types_by_name['CountResponse']
_GETREQUEST = DESCRIPTOR.message_types_by_name['GetRequest']
_GETRESPONSE = DESCRIPTOR.message_types_by_name['GetResponse']
_PUTREQUEST = DESCRIPTOR.message_types_by_name['PutRequest']
_PUTRESPONSE = DESCRIPTOR.message_types_by_name['PutResponse']
_GETALLREQUEST = DESCRIPTOR.message_types_by_name['GetAllRequest']
_DELETEREQUEST = DESCRIPTOR.message_types_by_name['DeleteRequest']
_DELETERESPONSE = DESCRIPTOR.message_types_by_name['DeleteResponse']
_MAPPARTITIONSWITHINDEXREQUEST = DESCRIPTOR.message_types_by_name['MapPartitionsWithIndexRequest']
_REDUCERESPONSE = DESCRIPTOR.message_types_by_name['ReduceResponse']
_AGGREGATEREQUEST = DESCRIPTOR.message_types_by_name['AggregateRequest']
_AGGREGATERESPONSE = DESCRIPTOR.message_types_by_name['AggregateResponse']
_WITHSTORESRESPONSE = DESCRIPTOR.message_types_by_name['WithStoresResponse']
CountResponse = _reflection.GeneratedProtocolMessageType('CountResponse', (_message.Message,), {
  'DESCRIPTOR' : _COUNTRESPONSE,
  '__module__' : 'egg_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.eggroll.core.egg.CountResponse)
  })
_sym_db.RegisterMessage(CountResponse)

GetRequest = _reflection.GeneratedProtocolMessageType('GetRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETREQUEST,
  '__module__' : 'egg_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.eggroll.core.egg.GetRequest)
  })
_sym_db.RegisterMessage(GetRequest)

GetResponse = _reflection.GeneratedProtocolMessageType('GetResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETRESPONSE,
  '__module__' : 'egg_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.eggroll.core.egg.GetResponse)
  })
_sym_db.RegisterMessage(GetResponse)

PutRequest = _reflection.GeneratedProtocolMessageType('PutRequest', (_message.Message,), {
  'DESCRIPTOR' : _PUTREQUEST,
  '__module__' : 'egg_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.eggroll.core.egg.PutRequest)
  })
_sym_db.RegisterMessage(PutRequest)

PutResponse = _reflection.GeneratedProtocolMessageType('PutResponse', (_message.Message,), {
  'DESCRIPTOR' : _PUTRESPONSE,
  '__module__' : 'egg_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.eggroll.core.egg.PutResponse)
  })
_sym_db.RegisterMessage(PutResponse)

GetAllRequest = _reflection.GeneratedProtocolMessageType('GetAllRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETALLREQUEST,
  '__module__' : 'egg_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.eggroll.core.egg.GetAllRequest)
  })
_sym_db.RegisterMessage(GetAllRequest)

DeleteRequest = _reflection.GeneratedProtocolMessageType('DeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEREQUEST,
  '__module__' : 'egg_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.eggroll.core.egg.DeleteRequest)
  })
_sym_db.RegisterMessage(DeleteRequest)

DeleteResponse = _reflection.GeneratedProtocolMessageType('DeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETERESPONSE,
  '__module__' : 'egg_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.eggroll.core.egg.DeleteResponse)
  })
_sym_db.RegisterMessage(DeleteResponse)

MapPartitionsWithIndexRequest = _reflection.GeneratedProtocolMessageType('MapPartitionsWithIndexRequest', (_message.Message,), {
  'DESCRIPTOR' : _MAPPARTITIONSWITHINDEXREQUEST,
  '__module__' : 'egg_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.eggroll.core.egg.MapPartitionsWithIndexRequest)
  })
_sym_db.RegisterMessage(MapPartitionsWithIndexRequest)

ReduceResponse = _reflection.GeneratedProtocolMessageType('ReduceResponse', (_message.Message,), {
  'DESCRIPTOR' : _REDUCERESPONSE,
  '__module__' : 'egg_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.eggroll.core.egg.ReduceResponse)
  })
_sym_db.RegisterMessage(ReduceResponse)

AggregateRequest = _reflection.GeneratedProtocolMessageType('AggregateRequest', (_message.Message,), {
  'DESCRIPTOR' : _AGGREGATEREQUEST,
  '__module__' : 'egg_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.eggroll.core.egg.AggregateRequest)
  })
_sym_db.RegisterMessage(AggregateRequest)

AggregateResponse = _reflection.GeneratedProtocolMessageType('AggregateResponse', (_message.Message,), {
  'DESCRIPTOR' : _AGGREGATERESPONSE,
  '__module__' : 'egg_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.eggroll.core.egg.AggregateResponse)
  })
_sym_db.RegisterMessage(AggregateResponse)

WithStoresResponse = _reflection.GeneratedProtocolMessageType('WithStoresResponse', (_message.Message,), {
  'DESCRIPTOR' : _WITHSTORESRESPONSE,
  '__module__' : 'egg_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.eggroll.core.egg.WithStoresResponse)
  })
_sym_db.RegisterMessage(WithStoresResponse)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _COUNTRESPONSE._serialized_start=42
  _COUNTRESPONSE._serialized_end=72
  _GETREQUEST._serialized_start=74
  _GETREQUEST._serialized_end=99
  _GETRESPONSE._serialized_start=101
  _GETRESPONSE._serialized_end=158
  _PUTREQUEST._serialized_start=160
  _PUTREQUEST._serialized_end=200
  _PUTRESPONSE._serialized_start=202
  _PUTRESPONSE._serialized_end=260
  _GETALLREQUEST._serialized_start=262
  _GETALLREQUEST._serialized_end=292
  _DELETEREQUEST._serialized_start=294
  _DELETEREQUEST._serialized_end=322
  _DELETERESPONSE._serialized_start=324
  _DELETERESPONSE._serialized_end=370
  _MAPPARTITIONSWITHINDEXREQUEST._serialized_start=372
  _MAPPARTITIONSWITHINDEXREQUEST._serialized_end=420
  _REDUCERESPONSE._serialized_start=422
  _REDUCERESPONSE._serialized_end=465
  _AGGREGATEREQUEST._serialized_start=467
  _AGGREGATEREQUEST._serialized_end=505
  _AGGREGATERESPONSE._serialized_start=507
  _AGGREGATERESPONSE._serialized_end=553
  _WITHSTORESRESPONSE._serialized_start=555
  _WITHSTORESRESPONSE._serialized_end=602
# @@protoc_insertion_point(module_scope)