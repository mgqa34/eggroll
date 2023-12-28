# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: deepspeed.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
import meta_pb2 as meta__pb2
import containers_pb2 as containers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x64\x65\x65pspeed.proto\x12\x1c\x63om.webank.eggroll.core.meta\x1a\x1egoogle/protobuf/duration.proto\x1a\nmeta.proto\x1a\x10\x63ontainers.proto\"=\n\x0fStoreSetRequest\x12\x0e\n\x06prefix\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\x0c\x12\r\n\x05value\x18\x03 \x01(\x0c\"\x12\n\x10StoreSetResponse\"Z\n\x0fStoreGetRequest\x12\x0e\n\x06prefix\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\x0c\x12*\n\x07timeout\x18\x03 \x01(\x0b\x32\x19.google.protobuf.Duration\"5\n\x10StoreGetResponse\x12\r\n\x05value\x18\x01 \x01(\x0c\x12\x12\n\nis_timeout\x18\x02 \x01(\x08\">\n\x0fStoreAddRequest\x12\x0e\n\x06prefix\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\x0c\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x03\"\"\n\x10StoreAddResponse\x12\x0e\n\x06\x61mount\x18\x01 \x01(\x03\"X\n\x19StoreCompareAndSetRequest\x12\x0e\n\x06prefix\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x0e\n\x06\x65xpect\x18\x03 \x01(\t\x12\x0e\n\x06update\x18\x04 \x01(\t\"\x1c\n\x1aStoreCompareAndSetResponse\"[\n\x10StoreWaitRequest\x12\x0e\n\x06prefix\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12*\n\x07timeout\x18\x03 \x01(\x0b\x32\x19.google.protobuf.Duration\"\x13\n\x11StoreWaitResponse\"%\n\x13StoreNumKeysRequest\x12\x0e\n\x06prefix\x18\x01 \x01(\t\"(\n\x14StoreNumKeysResponse\x12\x10\n\x08num_keys\x18\x01 \x01(\x03\"4\n\x15StoreDeleteKeyRequest\x12\x0e\n\x06prefix\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\")\n\x16StoreDeleteKeyResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"%\n\x13StoreDestroyRequest\x12\x0e\n\x06prefix\x18\x01 \x01(\t\"\'\n\x14StoreDestroyResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\xe5\x05\n\x10SubmitJobRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08job_type\x18\x03 \x01(\t\x12\x12\n\nworld_size\x18\x04 \x01(\r\x12\x19\n\x11\x63ommand_arguments\x18\x05 \x03(\t\x12g\n\x15\x65nvironment_variables\x18\x06 \x03(\x0b\x32H.com.webank.eggroll.core.meta.SubmitJobRequest.EnvironmentVariablesEntry\x12H\n\x05\x66iles\x18\x07 \x03(\x0b\x32\x39.com.webank.eggroll.core.meta.SubmitJobRequest.FilesEntry\x12U\n\x0czipped_files\x18\x08 \x03(\x0b\x32?.com.webank.eggroll.core.meta.SubmitJobRequest.ZippedFilesEntry\x12G\n\x10resource_options\x18\t \x01(\x0b\x32-.com.webank.eggroll.core.meta.ResourceOptions\x12L\n\x07options\x18\x13 \x03(\x0b\x32;.com.webank.eggroll.core.meta.SubmitJobRequest.OptionsEntry\x1a;\n\x19\x45nvironmentVariablesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a,\n\nFilesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\x1a\x32\n\x10ZippedFilesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\x1a.\n\x0cOptionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"O\n\x0fResourceOptions\x12\x17\n\x0ftimeout_seconds\x18\x01 \x01(\r\x12#\n\x1bresource_exhausted_strategy\x18\x02 \x01(\t\"d\n\x11SubmitJobResponse\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12;\n\nprocessors\x18\x02 \x03(\x0b\x32\'.com.webank.eggroll.core.meta.Processor\"$\n\x0eKillJobRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\"%\n\x0fKillJobResponse\x12\x12\n\nsession_id\x18\x01 \x01(\t\"$\n\x0eStopJobRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\"%\n\x0fStopJobResponse\x12\x12\n\nsession_id\x18\x01 \x01(\t\"%\n\x0fQueryJobRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\"\x85\x01\n\x10QueryJobResponse\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x10\n\x08job_type\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\t\x12;\n\nprocessors\x18\x05 \x03(\x0b\x32\'.com.webank.eggroll.core.meta.Processor\"+\n\x15QueryJobStatusRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\"<\n\x16QueryJobStatusResponse\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\"\xa9\x01\n\x12\x44ownloadJobRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\r\n\x05ranks\x18\x02 \x03(\x05\x12\x17\n\x0f\x63ompress_method\x18\x03 \x01(\t\x12\x16\n\x0e\x63ompress_level\x18\x04 \x01(\x05\x12?\n\x0c\x63ontent_type\x18\x05 \x01(\x0e\x32).com.webank.eggroll.core.meta.ContentType\"t\n\x13\x44ownloadJobResponse\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12I\n\x11\x63ontainer_content\x18\x02 \x03(\x0b\x32..com.webank.eggroll.core.meta.ContainerContent2\xb2\x06\n\x18\x44\x65\x65pspeedRendezvousStore\x12\x66\n\x03Set\x12-.com.webank.eggroll.core.meta.StoreSetRequest\x1a..com.webank.eggroll.core.meta.StoreSetResponse\"\x00\x12\x66\n\x03Get\x12-.com.webank.eggroll.core.meta.StoreGetRequest\x1a..com.webank.eggroll.core.meta.StoreGetResponse\"\x00\x12\x66\n\x03\x41\x64\x64\x12-.com.webank.eggroll.core.meta.StoreAddRequest\x1a..com.webank.eggroll.core.meta.StoreAddResponse\"\x00\x12\x84\x01\n\rCompareAndSet\x12\x37.com.webank.eggroll.core.meta.StoreCompareAndSetRequest\x1a\x38.com.webank.eggroll.core.meta.StoreCompareAndSetResponse\"\x00\x12i\n\x04Wait\x12..com.webank.eggroll.core.meta.StoreWaitRequest\x1a/.com.webank.eggroll.core.meta.StoreWaitResponse\"\x00\x12r\n\x07NumKeys\x12\x31.com.webank.eggroll.core.meta.StoreNumKeysRequest\x1a\x32.com.webank.eggroll.core.meta.StoreNumKeysResponse\"\x00\x12x\n\tDeleteKey\x12\x33.com.webank.eggroll.core.meta.StoreDeleteKeyRequest\x1a\x34.com.webank.eggroll.core.meta.StoreDeleteKeyResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'deepspeed_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _SUBMITJOBREQUEST_ENVIRONMENTVARIABLESENTRY._options = None
  _SUBMITJOBREQUEST_ENVIRONMENTVARIABLESENTRY._serialized_options = b'8\001'
  _SUBMITJOBREQUEST_FILESENTRY._options = None
  _SUBMITJOBREQUEST_FILESENTRY._serialized_options = b'8\001'
  _SUBMITJOBREQUEST_ZIPPEDFILESENTRY._options = None
  _SUBMITJOBREQUEST_ZIPPEDFILESENTRY._serialized_options = b'8\001'
  _SUBMITJOBREQUEST_OPTIONSENTRY._options = None
  _SUBMITJOBREQUEST_OPTIONSENTRY._serialized_options = b'8\001'
  _globals['_STORESETREQUEST']._serialized_start=111
  _globals['_STORESETREQUEST']._serialized_end=172
  _globals['_STORESETRESPONSE']._serialized_start=174
  _globals['_STORESETRESPONSE']._serialized_end=192
  _globals['_STOREGETREQUEST']._serialized_start=194
  _globals['_STOREGETREQUEST']._serialized_end=284
  _globals['_STOREGETRESPONSE']._serialized_start=286
  _globals['_STOREGETRESPONSE']._serialized_end=339
  _globals['_STOREADDREQUEST']._serialized_start=341
  _globals['_STOREADDREQUEST']._serialized_end=403
  _globals['_STOREADDRESPONSE']._serialized_start=405
  _globals['_STOREADDRESPONSE']._serialized_end=439
  _globals['_STORECOMPAREANDSETREQUEST']._serialized_start=441
  _globals['_STORECOMPAREANDSETREQUEST']._serialized_end=529
  _globals['_STORECOMPAREANDSETRESPONSE']._serialized_start=531
  _globals['_STORECOMPAREANDSETRESPONSE']._serialized_end=559
  _globals['_STOREWAITREQUEST']._serialized_start=561
  _globals['_STOREWAITREQUEST']._serialized_end=652
  _globals['_STOREWAITRESPONSE']._serialized_start=654
  _globals['_STOREWAITRESPONSE']._serialized_end=673
  _globals['_STORENUMKEYSREQUEST']._serialized_start=675
  _globals['_STORENUMKEYSREQUEST']._serialized_end=712
  _globals['_STORENUMKEYSRESPONSE']._serialized_start=714
  _globals['_STORENUMKEYSRESPONSE']._serialized_end=754
  _globals['_STOREDELETEKEYREQUEST']._serialized_start=756
  _globals['_STOREDELETEKEYREQUEST']._serialized_end=808
  _globals['_STOREDELETEKEYRESPONSE']._serialized_start=810
  _globals['_STOREDELETEKEYRESPONSE']._serialized_end=851
  _globals['_STOREDESTROYREQUEST']._serialized_start=853
  _globals['_STOREDESTROYREQUEST']._serialized_end=890
  _globals['_STOREDESTROYRESPONSE']._serialized_start=892
  _globals['_STOREDESTROYRESPONSE']._serialized_end=931
  _globals['_SUBMITJOBREQUEST']._serialized_start=934
  _globals['_SUBMITJOBREQUEST']._serialized_end=1675
  _globals['_SUBMITJOBREQUEST_ENVIRONMENTVARIABLESENTRY']._serialized_start=1470
  _globals['_SUBMITJOBREQUEST_ENVIRONMENTVARIABLESENTRY']._serialized_end=1529
  _globals['_SUBMITJOBREQUEST_FILESENTRY']._serialized_start=1531
  _globals['_SUBMITJOBREQUEST_FILESENTRY']._serialized_end=1575
  _globals['_SUBMITJOBREQUEST_ZIPPEDFILESENTRY']._serialized_start=1577
  _globals['_SUBMITJOBREQUEST_ZIPPEDFILESENTRY']._serialized_end=1627
  _globals['_SUBMITJOBREQUEST_OPTIONSENTRY']._serialized_start=1629
  _globals['_SUBMITJOBREQUEST_OPTIONSENTRY']._serialized_end=1675
  _globals['_RESOURCEOPTIONS']._serialized_start=1677
  _globals['_RESOURCEOPTIONS']._serialized_end=1756
  _globals['_SUBMITJOBRESPONSE']._serialized_start=1758
  _globals['_SUBMITJOBRESPONSE']._serialized_end=1858
  _globals['_KILLJOBREQUEST']._serialized_start=1860
  _globals['_KILLJOBREQUEST']._serialized_end=1896
  _globals['_KILLJOBRESPONSE']._serialized_start=1898
  _globals['_KILLJOBRESPONSE']._serialized_end=1935
  _globals['_STOPJOBREQUEST']._serialized_start=1937
  _globals['_STOPJOBREQUEST']._serialized_end=1973
  _globals['_STOPJOBRESPONSE']._serialized_start=1975
  _globals['_STOPJOBRESPONSE']._serialized_end=2012
  _globals['_QUERYJOBREQUEST']._serialized_start=2014
  _globals['_QUERYJOBREQUEST']._serialized_end=2051
  _globals['_QUERYJOBRESPONSE']._serialized_start=2054
  _globals['_QUERYJOBRESPONSE']._serialized_end=2187
  _globals['_QUERYJOBSTATUSREQUEST']._serialized_start=2189
  _globals['_QUERYJOBSTATUSREQUEST']._serialized_end=2232
  _globals['_QUERYJOBSTATUSRESPONSE']._serialized_start=2234
  _globals['_QUERYJOBSTATUSRESPONSE']._serialized_end=2294
  _globals['_DOWNLOADJOBREQUEST']._serialized_start=2297
  _globals['_DOWNLOADJOBREQUEST']._serialized_end=2466
  _globals['_DOWNLOADJOBRESPONSE']._serialized_start=2468
  _globals['_DOWNLOADJOBRESPONSE']._serialized_end=2584
  _globals['_DEEPSPEEDRENDEZVOUSSTORE']._serialized_start=2587
  _globals['_DEEPSPEEDRENDEZVOUSSTORE']._serialized_end=3405
# @@protoc_insertion_point(module_scope)
