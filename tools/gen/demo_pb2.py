# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: demo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='demo.proto',
  package='',
  serialized_pb=_b('\n\ndemo.proto\" \n\x04\x44\x65mo\x12\n\n\x02id\x18\x01 \x02(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\" \n\tDemoTable\x12\x13\n\x04list\x18\x01 \x02(\x0b\x32\x05.Demo')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DEMO = _descriptor.Descriptor(
  name='Demo',
  full_name='Demo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Demo.id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='Demo.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=46,
)


_DEMOTABLE = _descriptor.Descriptor(
  name='DemoTable',
  full_name='DemoTable',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='list', full_name='DemoTable.list', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=80,
)

_DEMOTABLE.fields_by_name['list'].message_type = _DEMO
DESCRIPTOR.message_types_by_name['Demo'] = _DEMO
DESCRIPTOR.message_types_by_name['DemoTable'] = _DEMOTABLE

Demo = _reflection.GeneratedProtocolMessageType('Demo', (_message.Message,), dict(
  DESCRIPTOR = _DEMO,
  __module__ = 'demo_pb2'
  # @@protoc_insertion_point(class_scope:Demo)
  ))
_sym_db.RegisterMessage(Demo)

DemoTable = _reflection.GeneratedProtocolMessageType('DemoTable', (_message.Message,), dict(
  DESCRIPTOR = _DEMOTABLE,
  __module__ = 'demo_pb2'
  # @@protoc_insertion_point(class_scope:DemoTable)
  ))
_sym_db.RegisterMessage(DemoTable)


# @@protoc_insertion_point(module_scope)