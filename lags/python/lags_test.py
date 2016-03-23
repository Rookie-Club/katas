import unittest

def gain_max():
    return 0

class LagsTest(unittest.TestCase):
    def test_0_sans_demande(self):
        self.assertEqual(0, gain_max())

unittest.main()
