# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: osmosis/gamm/v1beta1/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"osmosis/gamm/v1beta1/genesis.proto\x12\x14osmosis.gamm.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"\x8d\x01\n\x06Params\x12\x82\x01\n\x11pool_creation_fee\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBL\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xf2\xde\x1f\x18yaml:\"pool_creation_fee\"\xc8\xde\x1f\x00\"\x8c\x01\n\x0cGenesisState\x12.\n\x05pools\x18\x01 \x03(\x0b\x32\x14.google.protobuf.AnyB\t\xca\xb4-\x05PoolI\x12\x18\n\x10next_pool_number\x18\x02 \x01(\x04\x12\x32\n\x06params\x18\x03 \x01(\x0b\x32\x1c.osmosis.gamm.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\x42\x31Z/github.com/osmosis-labs/osmosis/v9/x/gamm/typesb\x06proto3')



_PARAMS = DESCRIPTOR.message_types_by_name['Params']
_GENESISSTATE = DESCRIPTOR.message_types_by_name['GenesisState']
Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), {
  'DESCRIPTOR' : _PARAMS,
  '__module__' : 'osmosis.gamm.v1beta1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:osmosis.gamm.v1beta1.Params)
  })
_sym_db.RegisterMessage(Params)

GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {
  'DESCRIPTOR' : _GENESISSTATE,
  '__module__' : 'osmosis.gamm.v1beta1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:osmosis.gamm.v1beta1.GenesisState)
  })
_sym_db.RegisterMessage(GenesisState)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z/github.com/osmosis-labs/osmosis/v9/x/gamm/types'
  _PARAMS.fields_by_name['pool_creation_fee']._options = None
  _PARAMS.fields_by_name['pool_creation_fee']._serialized_options = b'\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\362\336\037\030yaml:\"pool_creation_fee\"\310\336\037\000'
  _GENESISSTATE.fields_by_name['pools']._options = None
  _GENESISSTATE.fields_by_name['pools']._serialized_options = b'\312\264-\005PoolI'
  _GENESISSTATE.fields_by_name['params']._options = None
  _GENESISSTATE.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _PARAMS._serialized_start=169
  _PARAMS._serialized_end=310
  _GENESISSTATE._serialized_start=313
  _GENESISSTATE._serialized_end=453
# @@protoc_insertion_point(module_scope)
