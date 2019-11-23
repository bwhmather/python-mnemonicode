import typing


def to_base(base: int, num: int) -> typing.List[int]:
    ...


def from_base(base: int, num: typing.Iterable[int]) -> int:
    ...


def chunk_sequence(data: bytes, size: int) -> typing.Iterator[bytes]:
    ...
