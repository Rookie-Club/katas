import unittest

from diamond import *

class DiamondTest(unittest.TestCase):

    def test_for_B_display_ABBA(self):
        self.assertEqual(" A\nB B\n A", diamond("B"))

    def test_for_C_display_ABBCCBBA(self):
        self.assertEqual("  A\n B B\nC   C\n B B\n  A", diamond("C"))

if __name__ == "__main__":
    unittest.main()
