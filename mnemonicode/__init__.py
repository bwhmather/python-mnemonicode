from mnemonicode._wordlist import WORDLIST

MN_BASE = 1626


def _to_base(base, num):
    """Encode a positive integer as a big-endian list of digits in the given
    base
    """
    if num < 0:
        raise ValueError("only works on positive integers")

    out = []
    while num > 0:
        out.insert(0, num % base)
        num //= base
    return out

def _from_base(base, num):
    """Decode a big-endian iterable of digits in the given base to a single
    positive integer
    """
    out = 0
    for digit in num:
        if digit >= base or digit < 0:
            raise ValueError("invalid digit: %i" % digit)
        out *= base
        out += digit
    return out


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
