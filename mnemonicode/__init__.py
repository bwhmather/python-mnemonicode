from mnemonicode._wordlist import index_to_word, word_to_index

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


def _block_to_indices(block):
    if len(block) > 4:
        raise ValueError("block too big")

    # menmonicode uses little-endian numbers
    num = _from_base(256, reversed(block))

    base1626 = list(reversed(_to_base(1626, num)))

    # pad the word list to the correct size
    length = {
        1: 1,
        2: 2,
        3: 3,
        4: 3,
    }[len(block)]
    base1626 += [0] * (length - len(base1626))

    # The third byte in a block slightly leaks into the third word.  A
    # different set of words is used for this case to distinguish it from the
    # four byte case
    if len(block) == 3:
        base1626[2] += 1626

    return base1626


def _block_to_words(block):
    for i in _block_to_indices(block):
        yield index_to_word(i)


def _divide(data, size):
    """Split an iterator at `size` item intervals
    """
    for offset in range(0, len(data), size):
        yield data[offset:offset + size]


def mnencode(data):
    for block in _divide(data, 4):
        yield tuple(_block_to_words(block))


def _words_to_block(words):
    indices = list(word_to_index(word) for word in words)

    if len(indices) == 3:
        if indices[2] >= 1626:
            length = 3
            indices[2] -= 1626
        else:
            length = 4
    elif len(indices) in (1, 2):
        length = len(indices)
    else:
        raise ValueError("invalid length: %r" % indices)

    num = _from_base(1626, reversed(indices))

    block = bytes(reversed(_to_base(256, num)))

    return block.ljust(length, b'\x00')


def mndecode(data):
    return b''.join(_words_to_block(words) for words in data)
