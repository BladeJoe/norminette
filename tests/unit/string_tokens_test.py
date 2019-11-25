
import unittest
import sys
from lexer import Lexer

sys.path.append('../..')


class StringTokenTest(unittest.TestCase):

    def test_basic_string(self):
        self.assertEqual(
            Lexer('"Basic string"').getNextToken().test(),
            '<STRING="Basic string">')

    def test_basic_L_string(self):
        self.assertEqual(
              Lexer('L"Basic string"').getNextToken().test(),
              '<STRING=L"Basic string">')

    def test_basic_escaped_string(self):
        self.assertEqual(
              Lexer('"Basic \\"string\\""').getNextToken().test(),
              '<STRING="Basic \\"string\\"">')

    def test_escaped_string(self):
        self.assertEqual(
              Lexer('"Escaped \\\\\\"string\\\\\\\\\\\"\\\\"').getNextToken()
              .test(),
              '<STRING="Escaped \\\\\\"string\\\\\\\\\\\"\\\\">')


if __name__ == '__main__':
    unittest.main()
