import typing


WordGroup = typing.Union[
    typing.Tuple[str],
    typing.Tuple[str, str],
    typing.Tuple[str, str, str],
]


def mnencode(data: bytes) -> typing.Iterator[WordGroup]:
    ...


def mnformat(
    data: bytes, word_separator: str="-", group_separator: str="--",
) -> str:
    ...


def mndecode(data: typing.Iterator[WordGroup]) -> bytes:
    ...


def mnparse(
    string: str, word_separator: str="-", group_separator: str="--",
) -> bytes:
    ...
