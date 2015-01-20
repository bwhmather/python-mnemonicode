import unittest

import mnemonicode


class TestMnemonicode(unittest.TestCase):
    def test_wordlist(self):
        self.assertEqual(len(mnemonicode.WORDLIST), 1633)

    def test_divide(self):
        self.assertEqual(
            list(mnemonicode.divide(b'12345678', 4)),
            [b'1234', b'5678']
        )

        self.assertEqual(
            list(mnemonicode.divide(b'1234567', 4)),
            [b'1234', b'567']
        )

        self.assertEqual(
            list(mnemonicode.divide(b'12345', 4)),
            [b'1234', b'5']
        )

    def test_block_to_words(self):
        def test(string, words):
            self.assertEqual(list(mnemonicode.block_to_words(string)), words)

        test(b"a", ["camera"])
        test(b"ab", ["zero", "albert"])
        test(b"abc", ["hazard", "velvet", "jet"])
        test(b"abcd", ["bogart", "atlas", "safari"])

    def test_examples(self):
        def test(string, words):
            self.assertEqual(list(mnemonicode.mnencode(string)), words)

        test(b"a", ["camera"])
        test(b"ab", ["zero", "albert"])
        test(b"abc", ["hazard", "velvet", "jet"])
        test(b"abcd", [
            "bogart", "atlas", "safari"])
        test(b"abcde", [
            "bogart", "atlas", "safari",
            "cannon",
        ])
        test(b"abcdef", [
            "bogart", "atlas", "safari",
            "david", "albino",
        ])
        test(b"abcdefg", [
            "bogart", "atlas", "safari",
            "emerald", "infant", "jet",
        ])
        test(b"abcdefgh", [
            "bogart", "atlas", "safari",
            "airport", "cabaret", "shock",
        ])


loader = unittest.TestLoader()
suite = unittest.TestSuite((
    loader.loadTestsFromTestCase(TestMnemonicode),
))
