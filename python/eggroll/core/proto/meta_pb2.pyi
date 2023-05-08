"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file

Copyright (c) 2019 - now, Eggroll Authors. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class Endpoint(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HOST_FIELD_NUMBER: builtins.int
    PORT_FIELD_NUMBER: builtins.int
    host: builtins.str
    port: builtins.int
    def __init__(
        self,
        *,
        host: builtins.str = ...,
        port: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["host", b"host", "port", b"port"]) -> None: ...

global___Endpoint = Endpoint

@typing_extensions.final
class ServerNode(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    CLUSTERID_FIELD_NUMBER: builtins.int
    ENDPOINT_FIELD_NUMBER: builtins.int
    NODETYPE_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    id: builtins.int
    name: builtins.str
    clusterId: builtins.int
    @property
    def endpoint(self) -> global___Endpoint: ...
    nodeType: builtins.str
    status: builtins.str
    def __init__(
        self,
        *,
        id: builtins.int = ...,
        name: builtins.str = ...,
        clusterId: builtins.int = ...,
        endpoint: global___Endpoint | None = ...,
        nodeType: builtins.str = ...,
        status: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["endpoint", b"endpoint"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["clusterId", b"clusterId", "endpoint", b"endpoint", "id", b"id", "name", b"name", "nodeType", b"nodeType", "status", b"status"]) -> None: ...

global___ServerNode = ServerNode

@typing_extensions.final
class ServerCluster(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    SERVERNODES_FIELD_NUMBER: builtins.int
    TAG_FIELD_NUMBER: builtins.int
    id: builtins.int
    name: builtins.str
    @property
    def serverNodes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ServerNode]: ...
    tag: builtins.str
    def __init__(
        self,
        *,
        id: builtins.int = ...,
        name: builtins.str = ...,
        serverNodes: collections.abc.Iterable[global___ServerNode] | None = ...,
        tag: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id", "name", b"name", "serverNodes", b"serverNodes", "tag", b"tag"]) -> None: ...

global___ServerCluster = ServerCluster

@typing_extensions.final
class Processor(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class OptionsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    ID_FIELD_NUMBER: builtins.int
    SERVERNODEID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    PROCESSORTYPE_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    COMMANDENDPOINT_FIELD_NUMBER: builtins.int
    TRANSFERENDPOINT_FIELD_NUMBER: builtins.int
    PID_FIELD_NUMBER: builtins.int
    OPTIONS_FIELD_NUMBER: builtins.int
    TAG_FIELD_NUMBER: builtins.int
    id: builtins.int
    serverNodeId: builtins.int
    name: builtins.str
    processorType: builtins.str
    status: builtins.str
    @property
    def commandEndpoint(self) -> global___Endpoint: ...
    @property
    def transferEndpoint(self) -> global___Endpoint: ...
    pid: builtins.int
    @property
    def options(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    tag: builtins.str
    def __init__(
        self,
        *,
        id: builtins.int = ...,
        serverNodeId: builtins.int = ...,
        name: builtins.str = ...,
        processorType: builtins.str = ...,
        status: builtins.str = ...,
        commandEndpoint: global___Endpoint | None = ...,
        transferEndpoint: global___Endpoint | None = ...,
        pid: builtins.int = ...,
        options: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        tag: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["commandEndpoint", b"commandEndpoint", "transferEndpoint", b"transferEndpoint"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["commandEndpoint", b"commandEndpoint", "id", b"id", "name", b"name", "options", b"options", "pid", b"pid", "processorType", b"processorType", "serverNodeId", b"serverNodeId", "status", b"status", "tag", b"tag", "transferEndpoint", b"transferEndpoint"]) -> None: ...

global___Processor = Processor

@typing_extensions.final
class ProcessorBatch(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    PROCESSORS_FIELD_NUMBER: builtins.int
    TAG_FIELD_NUMBER: builtins.int
    id: builtins.int
    name: builtins.str
    @property
    def processors(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Processor]: ...
    tag: builtins.str
    def __init__(
        self,
        *,
        id: builtins.int = ...,
        name: builtins.str = ...,
        processors: collections.abc.Iterable[global___Processor] | None = ...,
        tag: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id", "name", b"name", "processors", b"processors", "tag", b"tag"]) -> None: ...

global___ProcessorBatch = ProcessorBatch

@typing_extensions.final
class Functor(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class OptionsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    NAME_FIELD_NUMBER: builtins.int
    SERDES_FIELD_NUMBER: builtins.int
    BODY_FIELD_NUMBER: builtins.int
    OPTIONS_FIELD_NUMBER: builtins.int
    name: builtins.str
    serdes: builtins.str
    body: builtins.bytes
    @property
    def options(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        serdes: builtins.str = ...,
        body: builtins.bytes = ...,
        options: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["body", b"body", "name", b"name", "options", b"options", "serdes", b"serdes"]) -> None: ...

global___Functor = Functor

@typing_extensions.final
class Pair(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    key: builtins.bytes
    value: builtins.bytes
    def __init__(
        self,
        *,
        key: builtins.bytes = ...,
        value: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

global___Pair = Pair

@typing_extensions.final
class PairBatch(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PAIRS_FIELD_NUMBER: builtins.int
    @property
    def pairs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Pair]: ...
    def __init__(
        self,
        *,
        pairs: collections.abc.Iterable[global___Pair] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["pairs", b"pairs"]) -> None: ...

global___PairBatch = PairBatch

@typing_extensions.final
class StoreLocator(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    STORETYPE_FIELD_NUMBER: builtins.int
    NAMESPACE_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    PATH_FIELD_NUMBER: builtins.int
    TOTALPARTITIONS_FIELD_NUMBER: builtins.int
    PARTITIONER_FIELD_NUMBER: builtins.int
    SERDES_FIELD_NUMBER: builtins.int
    id: builtins.int
    storeType: builtins.str
    namespace: builtins.str
    name: builtins.str
    path: builtins.str
    totalPartitions: builtins.int
    partitioner: builtins.str
    serdes: builtins.str
    def __init__(
        self,
        *,
        id: builtins.int = ...,
        storeType: builtins.str = ...,
        namespace: builtins.str = ...,
        name: builtins.str = ...,
        path: builtins.str = ...,
        totalPartitions: builtins.int = ...,
        partitioner: builtins.str = ...,
        serdes: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id", "name", b"name", "namespace", b"namespace", "partitioner", b"partitioner", "path", b"path", "serdes", b"serdes", "storeType", b"storeType", "totalPartitions", b"totalPartitions"]) -> None: ...

global___StoreLocator = StoreLocator

@typing_extensions.final
class Store(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class OptionsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    STORELOCATOR_FIELD_NUMBER: builtins.int
    PARTITIONS_FIELD_NUMBER: builtins.int
    OPTIONS_FIELD_NUMBER: builtins.int
    @property
    def storeLocator(self) -> global___StoreLocator: ...
    @property
    def partitions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Partition]: ...
    @property
    def options(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    def __init__(
        self,
        *,
        storeLocator: global___StoreLocator | None = ...,
        partitions: collections.abc.Iterable[global___Partition] | None = ...,
        options: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["storeLocator", b"storeLocator"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["options", b"options", "partitions", b"partitions", "storeLocator", b"storeLocator"]) -> None: ...

global___Store = Store

@typing_extensions.final
class StoreList(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STORES_FIELD_NUMBER: builtins.int
    @property
    def stores(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Store]: ...
    def __init__(
        self,
        *,
        stores: collections.abc.Iterable[global___Store] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["stores", b"stores"]) -> None: ...

global___StoreList = StoreList

@typing_extensions.final
class Partition(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    STORELOCATOR_FIELD_NUMBER: builtins.int
    PROCESSOR_FIELD_NUMBER: builtins.int
    SERVERNODEID_FIELD_NUMBER: builtins.int
    RANKINNODE_FIELD_NUMBER: builtins.int
    id: builtins.int
    @property
    def storeLocator(self) -> global___StoreLocator: ...
    @property
    def processor(self) -> global___Processor: ...
    serverNodeId: builtins.int
    rankInNode: builtins.int
    def __init__(
        self,
        *,
        id: builtins.int = ...,
        storeLocator: global___StoreLocator | None = ...,
        processor: global___Processor | None = ...,
        serverNodeId: builtins.int = ...,
        rankInNode: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["processor", b"processor", "storeLocator", b"storeLocator"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id", "processor", b"processor", "rankInNode", b"rankInNode", "serverNodeId", b"serverNodeId", "storeLocator", b"storeLocator"]) -> None: ...

global___Partition = Partition

@typing_extensions.final
class CallInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CALLSEQ_FIELD_NUMBER: builtins.int
    callSeq: builtins.str
    def __init__(
        self,
        *,
        callSeq: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["callSeq", b"callSeq"]) -> None: ...

global___CallInfo = CallInfo

@typing_extensions.final
class Job(google.protobuf.message.Message):
    """todo: add job / task status"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class OptionsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    INPUTS_FIELD_NUMBER: builtins.int
    OUTPUTS_FIELD_NUMBER: builtins.int
    FUNCTORS_FIELD_NUMBER: builtins.int
    OPTIONS_FIELD_NUMBER: builtins.int
    id: builtins.str
    name: builtins.str
    @property
    def inputs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Store]: ...
    @property
    def outputs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Store]: ...
    @property
    def functors(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Functor]: ...
    @property
    def options(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        name: builtins.str = ...,
        inputs: collections.abc.Iterable[global___Store] | None = ...,
        outputs: collections.abc.Iterable[global___Store] | None = ...,
        functors: collections.abc.Iterable[global___Functor] | None = ...,
        options: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["functors", b"functors", "id", b"id", "inputs", b"inputs", "name", b"name", "options", b"options", "outputs", b"outputs"]) -> None: ...

global___Job = Job

@typing_extensions.final
class Task(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    INPUTS_FIELD_NUMBER: builtins.int
    OUTPUTS_FIELD_NUMBER: builtins.int
    JOB_FIELD_NUMBER: builtins.int
    id: builtins.str
    name: builtins.str
    @property
    def inputs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Partition]: ...
    @property
    def outputs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Partition]: ...
    @property
    def job(self) -> global___Job: ...
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        name: builtins.str = ...,
        inputs: collections.abc.Iterable[global___Partition] | None = ...,
        outputs: collections.abc.Iterable[global___Partition] | None = ...,
        job: global___Job | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["job", b"job"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id", "inputs", b"inputs", "job", b"job", "name", b"name", "outputs", b"outputs"]) -> None: ...

global___Task = Task

@typing_extensions.final
class SessionMeta(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class OptionsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    TAG_FIELD_NUMBER: builtins.int
    PROCESSORS_FIELD_NUMBER: builtins.int
    OPTIONS_FIELD_NUMBER: builtins.int
    id: builtins.str
    name: builtins.str
    status: builtins.str
    tag: builtins.str
    @property
    def processors(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Processor]: ...
    @property
    def options(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        name: builtins.str = ...,
        status: builtins.str = ...,
        tag: builtins.str = ...,
        processors: collections.abc.Iterable[global___Processor] | None = ...,
        options: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id", "name", b"name", "options", b"options", "processors", b"processors", "status", b"status", "tag", b"tag"]) -> None: ...

global___SessionMeta = SessionMeta

@typing_extensions.final
class JobMeta(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class EnvironmentVariablesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    @typing_extensions.final
    class FilesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.bytes
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.bytes = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    @typing_extensions.final
    class ZippedFilesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.bytes
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.bytes = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    @typing_extensions.final
    class OptionsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    JOB_TYPE_FIELD_NUMBER: builtins.int
    WORLD_SIZE_FIELD_NUMBER: builtins.int
    COMMAND_ARGUMENTS_FIELD_NUMBER: builtins.int
    ENVIRONMENT_VARIABLES_FIELD_NUMBER: builtins.int
    FILES_FIELD_NUMBER: builtins.int
    ZIPPED_FILES_FIELD_NUMBER: builtins.int
    OPTIONS_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    PROCESSORS_FIELD_NUMBER: builtins.int
    id: builtins.str
    name: builtins.str
    job_type: builtins.str
    world_size: builtins.int
    @property
    def command_arguments(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def environment_variables(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    @property
    def files(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.bytes]: ...
    @property
    def zipped_files(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.bytes]: ...
    @property
    def options(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    status: builtins.str
    @property
    def processors(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Processor]: ...
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        name: builtins.str = ...,
        job_type: builtins.str = ...,
        world_size: builtins.int = ...,
        command_arguments: collections.abc.Iterable[builtins.str] | None = ...,
        environment_variables: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        files: collections.abc.Mapping[builtins.str, builtins.bytes] | None = ...,
        zipped_files: collections.abc.Mapping[builtins.str, builtins.bytes] | None = ...,
        options: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        status: builtins.str = ...,
        processors: collections.abc.Iterable[global___Processor] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["command_arguments", b"command_arguments", "environment_variables", b"environment_variables", "files", b"files", "id", b"id", "job_type", b"job_type", "name", b"name", "options", b"options", "processors", b"processors", "status", b"status", "world_size", b"world_size", "zipped_files", b"zipped_files"]) -> None: ...

global___JobMeta = JobMeta