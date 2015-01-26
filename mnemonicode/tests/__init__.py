import unittest

import mnemonicode
from mnemonicode import _to_base, _from_base


class TestBaseConversion(unittest.TestCase):
    def test_encode_zero(self):
        self.assertEqual([], _to_base(12, 0))

    def test_encode_base_ten(self):
        self.assertEqual([1, 2, 3, 4, 5, 6], _to_base(10, 123456))

    def test_encode_negative(self):
        self.assertRaises(ValueError, _to_base, 64, -10)

    def test_decode_base_ten(self):
        self.assertEqual(123456, _from_base(10, [1, 2, 3, 4, 5, 6]))

    def test_decode_zero(self):
        self.assertEqual(0, _from_base(16, []))

    def test_decode_empty_digits(self):
        self.assertEqual(456, _from_base(10, [0, 0, 0, 4, 5, 6]))

    def test_decode_invalid_digits(self):
        self.assertRaises(ValueError, _from_base, 8, [128])
        self.assertRaises(ValueError, _from_base, 8, [8])


class TestMnemonicode(unittest.TestCase):
    def test_wordlist(self):
        self.assertEqual(len(mnemonicode.WORDLIST), 1633)

    def test_divide(self):
        self.assertEqual(
            list(mnemonicode._divide(b'12345678', 4)),
            [b'1234', b'5678']
        )

        self.assertEqual(
            list(mnemonicode._divide(b'1234567', 4)),
            [b'1234', b'567']
        )

        self.assertEqual(
            list(mnemonicode._divide(b'12345', 4)),
            [b'1234', b'5']
        )

    def test_block_to_words(self):
        def test(string, words):
            self.assertEqual(tuple(mnemonicode._block_to_words(string)), words)

        test(b"a", ("camera",))
        test(b"ab", ("zero", "albert"))
        test(b"abc", ("hazard", "velvet", "jet"))
        test(b"abcd", ("bogart", "atlas", "safari"))

    def test_examples(self):
        def test(string, words):
            self.assertEqual(list(mnemonicode.mnencode(string)), words)

        test(b"a", [("camera",)])
        test(b"ab", [("zero", "albert")])
        test(b"abc", [("hazard", "velvet", "jet")])
        test(b"abcd", [
            ("bogart", "atlas", "safari")])
        test(b"abcde", [
            ("bogart", "atlas", "safari"),
            ("cannon",),
        ])
        test(b"abcdef", [
            ("bogart", "atlas", "safari"),
            ("david", "albino"),
        ])
        test(b"abcdefg", [
            ("bogart", "atlas", "safari"),
            ("emerald", "infant", "jet"),
        ])
        test(b"abcdefgh", [
            ("bogart", "atlas", "safari"),
            ("airport", "cabaret", "shock"),
        ])


loader = unittest.TestLoader()
suite = unittest.TestSuite((
    loader.loadTestsFromTestCase(TestBaseConversion),
    loader.loadTestsFromTestCase(TestMnemonicode),
))
