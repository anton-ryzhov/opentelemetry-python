# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from opentelemetry.proto.logs.v1.logs_pb2 import (
    ResourceLogs as opentelemetry___proto___logs___v1___logs_pb2___ResourceLogs,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Union as typing___Union,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class ExportLogsServiceRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def resource_logs(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[opentelemetry___proto___logs___v1___logs_pb2___ResourceLogs]: ...

    def __init__(self,
        *,
        resource_logs : typing___Optional[typing___Iterable[opentelemetry___proto___logs___v1___logs_pb2___ResourceLogs]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ExportLogsServiceRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ExportLogsServiceRequest: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"resource_logs",b"resource_logs"]) -> None: ...
type___ExportLogsServiceRequest = ExportLogsServiceRequest

class ExportLogsServiceResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    def __init__(self,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ExportLogsServiceResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ExportLogsServiceResponse: ...
type___ExportLogsServiceResponse = ExportLogsServiceResponse
