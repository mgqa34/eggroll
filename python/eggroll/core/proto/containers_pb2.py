# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: containers.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x63ontainers.proto\x12\x1c\x63om.webank.eggroll.core.meta\"\xca\x06\n\x16StartContainersRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08job_type\x18\x03 \x01(\t\x12\x19\n\x11\x63ommand_arguments\x18\x04 \x03(\t\x12m\n\x15\x65nvironment_variables\x18\x05 \x03(\x0b\x32N.com.webank.eggroll.core.meta.StartContainersRequest.EnvironmentVariablesEntry\x12N\n\x05\x66iles\x18\x06 \x03(\x0b\x32?.com.webank.eggroll.core.meta.StartContainersRequest.FilesEntry\x12[\n\x0czipped_files\x18\x07 \x03(\x0b\x32\x45.com.webank.eggroll.core.meta.StartContainersRequest.ZippedFilesEntry\x12h\n\x13typed_extra_configs\x18\x08 \x03(\x0b\x32K.com.webank.eggroll.core.meta.StartContainersRequest.TypedExtraConfigsEntry\x12R\n\x07options\x18\t \x03(\x0b\x32\x41.com.webank.eggroll.core.meta.StartContainersRequest.OptionsEntry\x1a;\n\x19\x45nvironmentVariablesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a,\n\nFilesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\x1a\x32\n\x10ZippedFilesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\x1a\x38\n\x16TypedExtraConfigsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x04\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\x1a.\n\x0cOptionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xf9\x01\n\x18\x44\x65\x65pspeedContainerConfig\x12\x1c\n\x14\x63uda_visible_devices\x18\x02 \x03(\r\x12\x12\n\nworld_size\x18\x03 \x01(\r\x12\x12\n\ncross_rank\x18\x04 \x01(\r\x12\x12\n\ncross_size\x18\x05 \x01(\r\x12\x12\n\nlocal_size\x18\x06 \x01(\r\x12\x12\n\nlocal_rank\x18\x07 \x01(\r\x12\x0c\n\x04rank\x18\x08 \x01(\r\x12\x12\n\nstore_host\x18\t \x01(\t\x12\x12\n\nstore_port\x18\n \x01(\x05\x12\x14\n\x0cstore_prefix\x18\x0b \x01(\t\x12\x0f\n\x07\x62\x61\x63kend\x18\x0c \x01(\t\"-\n\x17StartContainersResponse\x12\x12\n\nsession_id\x18\x01 \x01(\t\"B\n\x15StopContainersRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x15\n\rcontainer_ids\x18\x02 \x03(\x03\",\n\x16StopContainersResponse\x12\x12\n\nsession_id\x18\x01 \x01(\t\"B\n\x15KillContainersRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x15\n\rcontainer_ids\x18\x02 \x03(\x03\",\n\x16KillContainersResponse\x12\x12\n\nsession_id\x18\x01 \x01(\t\"\xb0\x01\n\x19\x44ownloadContainersRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\r\n\x05ranks\x18\x02 \x03(\x05\x12\x17\n\x0f\x63ompress_method\x18\x03 \x01(\t\x12\x16\n\x0e\x63ompress_level\x18\x04 \x01(\x05\x12?\n\x0c\x63ontent_type\x18\x05 \x01(\x0e\x32).com.webank.eggroll.core.meta.ContentType\"{\n\x1a\x44ownloadContainersResponse\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12I\n\x11\x63ontainer_content\x18\x02 \x03(\x0b\x32..com.webank.eggroll.core.meta.ContainerContent\"J\n\x10\x43ontainerContent\x12\x0c\n\x04rank\x18\x01 \x01(\x05\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\x0c\x12\x17\n\x0f\x63ompress_method\x18\x03 \x01(\t*,\n\x0b\x43ontentType\x12\x07\n\x03\x41LL\x10\x00\x12\n\n\x06MODELS\x10\x01\x12\x08\n\x04LOGS\x10\x02\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'containers_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _STARTCONTAINERSREQUEST_ENVIRONMENTVARIABLESENTRY._options = None
  _STARTCONTAINERSREQUEST_ENVIRONMENTVARIABLESENTRY._serialized_options = b'8\001'
  _STARTCONTAINERSREQUEST_FILESENTRY._options = None
  _STARTCONTAINERSREQUEST_FILESENTRY._serialized_options = b'8\001'
  _STARTCONTAINERSREQUEST_ZIPPEDFILESENTRY._options = None
  _STARTCONTAINERSREQUEST_ZIPPEDFILESENTRY._serialized_options = b'8\001'
  _STARTCONTAINERSREQUEST_TYPEDEXTRACONFIGSENTRY._options = None
  _STARTCONTAINERSREQUEST_TYPEDEXTRACONFIGSENTRY._serialized_options = b'8\001'
  _STARTCONTAINERSREQUEST_OPTIONSENTRY._options = None
  _STARTCONTAINERSREQUEST_OPTIONSENTRY._serialized_options = b'8\001'
  _globals['_CONTENTTYPE']._serialized_start=1802
  _globals['_CONTENTTYPE']._serialized_end=1846
  _globals['_STARTCONTAINERSREQUEST']._serialized_start=51
  _globals['_STARTCONTAINERSREQUEST']._serialized_end=893
  _globals['_STARTCONTAINERSREQUEST_ENVIRONMENTVARIABLESENTRY']._serialized_start=630
  _globals['_STARTCONTAINERSREQUEST_ENVIRONMENTVARIABLESENTRY']._serialized_end=689
  _globals['_STARTCONTAINERSREQUEST_FILESENTRY']._serialized_start=691
  _globals['_STARTCONTAINERSREQUEST_FILESENTRY']._serialized_end=735
  _globals['_STARTCONTAINERSREQUEST_ZIPPEDFILESENTRY']._serialized_start=737
  _globals['_STARTCONTAINERSREQUEST_ZIPPEDFILESENTRY']._serialized_end=787
  _globals['_STARTCONTAINERSREQUEST_TYPEDEXTRACONFIGSENTRY']._serialized_start=789
  _globals['_STARTCONTAINERSREQUEST_TYPEDEXTRACONFIGSENTRY']._serialized_end=845
  _globals['_STARTCONTAINERSREQUEST_OPTIONSENTRY']._serialized_start=847
  _globals['_STARTCONTAINERSREQUEST_OPTIONSENTRY']._serialized_end=893
  _globals['_DEEPSPEEDCONTAINERCONFIG']._serialized_start=896
  _globals['_DEEPSPEEDCONTAINERCONFIG']._serialized_end=1145
  _globals['_STARTCONTAINERSRESPONSE']._serialized_start=1147
  _globals['_STARTCONTAINERSRESPONSE']._serialized_end=1192
  _globals['_STOPCONTAINERSREQUEST']._serialized_start=1194
  _globals['_STOPCONTAINERSREQUEST']._serialized_end=1260
  _globals['_STOPCONTAINERSRESPONSE']._serialized_start=1262
  _globals['_STOPCONTAINERSRESPONSE']._serialized_end=1306
  _globals['_KILLCONTAINERSREQUEST']._serialized_start=1308
  _globals['_KILLCONTAINERSREQUEST']._serialized_end=1374
  _globals['_KILLCONTAINERSRESPONSE']._serialized_start=1376
  _globals['_KILLCONTAINERSRESPONSE']._serialized_end=1420
  _globals['_DOWNLOADCONTAINERSREQUEST']._serialized_start=1423
  _globals['_DOWNLOADCONTAINERSREQUEST']._serialized_end=1599
  _globals['_DOWNLOADCONTAINERSRESPONSE']._serialized_start=1601
  _globals['_DOWNLOADCONTAINERSRESPONSE']._serialized_end=1724
  _globals['_CONTAINERCONTENT']._serialized_start=1726
  _globals['_CONTAINERCONTENT']._serialized_end=1800
# @@protoc_insertion_point(module_scope)
