def to_base(base, num):
    """Encode a positive integer as a big-endian list of digits in the given
    base.
    """
    if num < 0:
        raise ValueError("only works on positive integers")

    out = []
    while num > 0:
        out.insert(0, num % base)
        num //= base
    return out


def from_base(base, num):
    """Decode a big-endian iterable of digits in the given base to a single
    positive integer.
    """
    out = 0
    for digit in num:
        if digit >= base or digit < 0:
            raise ValueError("invalid digit: %i" % digit)
        out *= base
        out += digit
    return out


def chunk_sequence(data, size):
    """Split an iterator at ``size`` item intervals
    """
    for offset in range(0, len(data), size):
        yield data[offset:offset + size]
