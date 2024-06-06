# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: waterquality.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12waterquality.proto\x12\x10\x61pi.waterquality\"$\n\x08GeoPoint\x12\x0b\n\x03lat\x18\x01 \x01(\x01\x12\x0b\n\x03lon\x18\x02 \x01(\x01\"\x96\x01\n\x07Quality\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\x12-\n\tgeo_point\x18\x02 \x01(\x0b\x32\x1a.api.waterquality.GeoPoint\x12\x13\n\x0btemperature\x18\x03 \x01(\x02\x12\n\n\x02ph\x18\x04 \x01(\x02\x12\x0b\n\x03tsw\x18\x05 \x01(\x02\x12\x0b\n\x03tds\x18\x06 \x01(\x02\x12\x0e\n\x06oxygen\x18\x07 \x01(\x02\"^\n\nPredictReq\x12,\n\tqualities\x18\x01 \x03(\x0b\x32\x19.api.waterquality.Quality\x12\x11\n\tlook_back\x18\x02 \x01(\x03\x12\x0f\n\x07horizon\x18\x03 \x01(\x03\";\n\x0bPredictResp\x12,\n\tqualities\x18\x01 \x03(\x0b\x32\x19.api.waterquality.Quality\"\x1f\n\x0eGuessLevelResp\x12\r\n\x05level\x18\x01 \x01(\x03\"f\n\x12PredictAndGuessReq\x12,\n\tqualities\x18\x01 \x03(\x0b\x32\x19.api.waterquality.Quality\x12\x11\n\tlook_back\x18\x02 \x01(\x03\x12\x0f\n\x07horizon\x18\x03 \x01(\x03\"R\n\x13PredictAndGuessResp\x12,\n\tqualities\x18\x01 \x03(\x0b\x32\x19.api.waterquality.Quality\x12\r\n\x05level\x18\x02 \x03(\x03\x32\x8e\x02\n\x13WaterQualityService\x12H\n\x07Predict\x12\x1c.api.waterquality.PredictReq\x1a\x1d.api.waterquality.PredictResp\"\x00\x12K\n\nGuessLevel\x12\x19.api.waterquality.Quality\x1a .api.waterquality.GuessLevelResp\"\x00\x12`\n\x0fPredictAndGuess\x12$.api.waterquality.PredictAndGuessReq\x1a%.api.waterquality.PredictAndGuessResp\"\x00\x42HZFgithub.com/I-m-Surrounded-by-IoT/backend/api/waterquality;waterqualityb\x06proto3')



_GEOPOINT = DESCRIPTOR.message_types_by_name['GeoPoint']
_QUALITY = DESCRIPTOR.message_types_by_name['Quality']
_PREDICTREQ = DESCRIPTOR.message_types_by_name['PredictReq']
_PREDICTRESP = DESCRIPTOR.message_types_by_name['PredictResp']
_GUESSLEVELRESP = DESCRIPTOR.message_types_by_name['GuessLevelResp']
_PREDICTANDGUESSREQ = DESCRIPTOR.message_types_by_name['PredictAndGuessReq']
_PREDICTANDGUESSRESP = DESCRIPTOR.message_types_by_name['PredictAndGuessResp']
GeoPoint = _reflection.GeneratedProtocolMessageType('GeoPoint', (_message.Message,), {
  'DESCRIPTOR' : _GEOPOINT,
  '__module__' : 'waterquality_pb2'
  # @@protoc_insertion_point(class_scope:api.waterquality.GeoPoint)
  })
_sym_db.RegisterMessage(GeoPoint)

Quality = _reflection.GeneratedProtocolMessageType('Quality', (_message.Message,), {
  'DESCRIPTOR' : _QUALITY,
  '__module__' : 'waterquality_pb2'
  # @@protoc_insertion_point(class_scope:api.waterquality.Quality)
  })
_sym_db.RegisterMessage(Quality)

PredictReq = _reflection.GeneratedProtocolMessageType('PredictReq', (_message.Message,), {
  'DESCRIPTOR' : _PREDICTREQ,
  '__module__' : 'waterquality_pb2'
  # @@protoc_insertion_point(class_scope:api.waterquality.PredictReq)
  })
_sym_db.RegisterMessage(PredictReq)

PredictResp = _reflection.GeneratedProtocolMessageType('PredictResp', (_message.Message,), {
  'DESCRIPTOR' : _PREDICTRESP,
  '__module__' : 'waterquality_pb2'
  # @@protoc_insertion_point(class_scope:api.waterquality.PredictResp)
  })
_sym_db.RegisterMessage(PredictResp)

GuessLevelResp = _reflection.GeneratedProtocolMessageType('GuessLevelResp', (_message.Message,), {
  'DESCRIPTOR' : _GUESSLEVELRESP,
  '__module__' : 'waterquality_pb2'
  # @@protoc_insertion_point(class_scope:api.waterquality.GuessLevelResp)
  })
_sym_db.RegisterMessage(GuessLevelResp)

PredictAndGuessReq = _reflection.GeneratedProtocolMessageType('PredictAndGuessReq', (_message.Message,), {
  'DESCRIPTOR' : _PREDICTANDGUESSREQ,
  '__module__' : 'waterquality_pb2'
  # @@protoc_insertion_point(class_scope:api.waterquality.PredictAndGuessReq)
  })
_sym_db.RegisterMessage(PredictAndGuessReq)

PredictAndGuessResp = _reflection.GeneratedProtocolMessageType('PredictAndGuessResp', (_message.Message,), {
  'DESCRIPTOR' : _PREDICTANDGUESSRESP,
  '__module__' : 'waterquality_pb2'
  # @@protoc_insertion_point(class_scope:api.waterquality.PredictAndGuessResp)
  })
_sym_db.RegisterMessage(PredictAndGuessResp)

_WATERQUALITYSERVICE = DESCRIPTOR.services_by_name['WaterQualityService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZFgithub.com/I-m-Surrounded-by-IoT/backend/api/waterquality;waterquality'
  _GEOPOINT._serialized_start=40
  _GEOPOINT._serialized_end=76
  _QUALITY._serialized_start=79
  _QUALITY._serialized_end=229
  _PREDICTREQ._serialized_start=231
  _PREDICTREQ._serialized_end=325
  _PREDICTRESP._serialized_start=327
  _PREDICTRESP._serialized_end=386
  _GUESSLEVELRESP._serialized_start=388
  _GUESSLEVELRESP._serialized_end=419
  _PREDICTANDGUESSREQ._serialized_start=421
  _PREDICTANDGUESSREQ._serialized_end=523
  _PREDICTANDGUESSRESP._serialized_start=525
  _PREDICTANDGUESSRESP._serialized_end=607
  _WATERQUALITYSERVICE._serialized_start=610
  _WATERQUALITYSERVICE._serialized_end=880
# @@protoc_insertion_point(module_scope)
