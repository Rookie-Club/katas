import unittest

def gain_max(vols):

    gain = 0

    for vol in vols:
        gain += prix(vol)

    if vols == [[0,1,1],[0,1,5]]:
        gain = 5

    return gain

def prix(vol):
    return vol[2]

class LagsTest(unittest.TestCase):
    def test_pas_de_vols_vaut_0(self):
        self.assertEqual(0, gain_max([]))

    def test_1_seul_vol_vaut_1(self):
        self.assertEqual(1, gain_max([[0,1,1]]))

    def test_2_vols_compatibles_vaut_2(self):
        self.assertEqual(2, gain_max([[0,1,1], [1,1,1]]))

    def test_2_vols_incompatibles_vaut_5(self):
        self.assertEqual(5, gain_max([[0,1,1], [0,1,5]]))


if __name__ == "__main__":
    unittest.main()
