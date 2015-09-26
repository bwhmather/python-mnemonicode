import sys
import argparse

from mnemonicode._wordlist import index_to_word, word_to_index


def _to_base(base, num):
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


def _from_base(base, num):
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


def _block_to_indices(block):
    if len(block) > 4:
        raise ValueError("block too big")

    # menmonicode uses little-endian numbers
    num = _from_base(256, reversed(block))

    indices = list(reversed(_to_base(1626, num)))

    # pad the list of indices to the correct size
    length = {
        1: 1,
        2: 2,
        3: 3,
        4: 3,
    }[len(block)]
    indices += [0] * (length - len(indices))

    # The third byte in a block slightly leaks into the third word.  A
    # different set of words is used for this case to distinguish it from the
    # four byte case
    if len(block) == 3:
        indices[-1] += 1626

    return indices


def _block_to_words(block):
    for i in _block_to_indices(block):
        yield index_to_word(i)


def _divide(data, size):
    """Split an iterator at ``size`` item intervals
    """
    for offset in range(0, len(data), size):
        yield data[offset:offset + size]


def mnencode(data):
    """Encode a bytes object as an iterator of tuples of words.

    >>> list(mnencode(b"avocado"))
    [('bicycle', 'visible', 'robert'), ('cloud', 'unicorn', 'jet')]

    :param bytes data:
        The binary data to encode.
    :returns:
        A list of tuples of between one and three words from the wordlist.
    """
    if not isinstance(data, (bytes, bytearray)):
        raise TypeError(
            "expected bytes or bytearray, got %s" % type(data).__name__
        )
    for block in _divide(data, 4):
        yield tuple(_block_to_words(block))


def mnformat(data, word_separator="-", group_separator="--"):
    """Encode a byte array as a sequence of grouped words, formatted as a
    single string.

    >>> mnformat(b"cucumber")
    'paris-pearl-ultra--gentle-press-total'

    :param bytes data:
        The binary data to encode.
    :param str word_separator:
        String that should be used to separate words within a group.
    :param str word_separator:
        String that should be used to separate groups of words.
    :return str:
        The data as an sequence of grouped words.
    """
    return group_separator.join(
        word_separator.join(group) for group in mnencode(data)
    )


def _words_to_block(words):
    if not isinstance(words, tuple):
        raise TypeError("expected tuple of words")

    if len(words) == 0:
        raise ValueError("no words in block")

    if len(words) > 3:
        raise ValueError("too many words in block")

    try:
        indices = list(word_to_index(word) for word in words)
    except KeyError as e:
        raise ValueError("word not recognized") from e

    # calculate length of block.
    # both three byte and four byte blocks map to three words but can be
    # distinguished as a different word list is used to encode the last word
    # in the three byte case
    length = {
        1: 1,
        2: 2,
        3: 3 if indices[-1] >= 1626 else 4,
    }[len(words)]

    if length == 3:
        indices[2] -= 1626

    # check that words in the second word list don't appear anywhere else in
    # the block
    for index in indices:
        if index > 1626:
            raise ValueError(
                "unexpected three byte word: %s" % index_to_word(index)
            )

    num = _from_base(1626, reversed(indices))

    block = bytes(reversed(_to_base(256, num)))

    # pad to correct length
    return block.ljust(length, b'\x00')


def mndecode(data):
    """Decode an iterator of tuples of words to get a byte array

    >>> mndecode([('turtle', 'special', 'recycle'), ('ferrari', 'album')])
    b'potato'

    :param data:
        An iterator of tuples of between one and three words from the wordlist
    :return bytes:
        A :class:`bytes` object containing the decoded data
    """
    return b''.join(_words_to_block(words) for words in data)


def mnparse(string, word_separator="-", group_separator="--"):
    """Decode a mnemonicode string into a byte array.

    >>> mnparse('scoop-limit-recycle--ferrari-album')
    b'tomato'

    :param str string:
        The string containing the mnemonicode encoded data.
    :param str word_separator:
        String used to separate individual words in a group.
    :param str group_separator:
        String used to separate groups of words representing four byte blocks.
    :return bytes:
        A :class:`bytes` object containing the decoded data
    """
    if not isinstance(string, str):
        raise TypeError("expected string, got %s" % type(string).__name__)

    # empty string is a valid input but ``"".split(...)`` does not return an
    # empty iterator so we need to special case it
    if len(string) == 0:
        return b''

    return mndecode(
        tuple(group.split(word_separator))
        for group in string.split(group_separator)
    )


def _mnencode_main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--word-separator', type=str, default='-')
    parser.add_argument('-g', '--group-separator', type=str, default='--')
    parser.add_argument(
        'infile', nargs='?',
        type=argparse.FileType('rb'), default=sys.stdin.buffer
    )
    parser.add_argument(
        'outfile', nargs='?',
        type=argparse.FileType('w'), default=sys.stdout
    )
    args = parser.parse_args()

    args.outfile.write(mnformat(
        args.infile.read(),
        word_separator=args.word_separator,
        group_separator=args.group_separator,
    ))


def _mndecode_main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--word-separator', type=str, default='-')
    parser.add_argument('-g', '--group-separator', type=str, default='--')
    parser.add_argument(
        'infile', nargs='?',
        type=argparse.FileType('r'), default=sys.stdin
    )
    parser.add_argument(
        'outfile', nargs='?',
        type=argparse.FileType('wb'), default=sys.stdout.buffer
    )
    args = parser.parse_args()

    args.outfile.write(mnparse(
        args.infile.read().strip(),
        word_separator=args.word_separator,
        group_separator=args.group_separator,
    ))
