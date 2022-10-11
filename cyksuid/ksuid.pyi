import datetime
from typing import Callable, Optional

_bytestr = bytes

BYTE_LENGTH: int
STRING_ENCODED_LENGTH: int
EMPTY_BYTES: bytes
MAX_ENCODED: bytes

class KSUID:
    _bytes: bytes
    _data: bytes

    def __init__(self, s: bytes) -> None: ...
    def __lt__(self, other: object) -> bool: ...
    def __le__(self, other: object) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __bytes__(self) -> bytes: ...

    @property
    def datetime(self) -> datetime.datetime: ...
    @property
    def timestamp(self) -> int: ...
    @property
    def payload(self) -> _bytestr: ...
    @property
    def bytes(self) -> _bytestr: ...
    @property
    def hex(self) -> str: ...
    @property
    def encoded(self) -> _bytestr: ...

def from_bytes(s: bytes) -> KSUID: ...
def from_parts(timestamp: int, payload: bytes) -> KSUID: ...

TimeFunc = Callable[[], float]
RandFunc = Callable[[int], bytes]

def ksuid(
    time_func: Optional[TimeFunc] = None,
    rand_func: Optional[RandFunc] = None,
) -> KSUID: ...
def parse(s: bytes | str) -> KSUID: ...

# Represents a completely empty (invalid) KSUID
Empty: KSUID
