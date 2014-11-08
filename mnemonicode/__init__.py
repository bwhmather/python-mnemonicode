from mnemonicode._wordlist import WORDLIST

MN_BASE = 1626


def block_to_indeces(block):
    x = sum(
        block[i] * (2**(i*8))
        for i in range(len(block))
    )

    yield x % MN_BASE

    if len(block) >= 2:
        yield (x // MN_BASE) % MN_BASE

    if len(block) == 3:
        yield (x // (MN_BASE**2)) % MN_BASE + MN_BASE
    elif len(block) == 4:
        yield (x // (MN_BASE**2)) % MN_BASE


def block_to_words(block):
    for i in block_to_indeces(block):
        yield WORDLIST[i]


def divide(data, size):
    """Split an iterator at `size` item intervals
    """
    for offset in range(0, len(data), size):
        yield data[offset:offset + size]


def mnencode(data):
    for block in divide(data, 4):
        yield from block_to_words(block)
