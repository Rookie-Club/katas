import unittest
from langton import *

class LangtonTest(unittest.TestCase):
    def test_premier_pas(self):
        position, orientation, positions = parcours_fourmi([3, 3], [0, -1], [])
        self.assertEqual([1, 0], orientation)
        #self.assertEqual([[3, 3]], positions)
        #self.assertEqual([2, 3], position)

    def test_nouvelle_orientation_sans_cases_blanches(self):
        self.assertEqual([0, -1], nouvelle_orientation([0, 0], [-1, 0], []))
        self.assertEqual([1, 0], nouvelle_orientation([0, 0], [0, -1], []))
        self.assertEqual([0, 1], nouvelle_orientation([0, 0], [1, 0], []))
        self.assertEqual([-1, 0], nouvelle_orientation([0, 0], [0, 1], []))

    def test_nouvelle_orientation_en_etant_sur_une_case_blanche(self):
        self.assertEqual([0, 1], nouvelle_orientation([1, 0], [-1, 0], [[1, 0]]))
        self.assertEqual([-1, 0], nouvelle_orientation([1, 0], [0, -1], [[1, 0]]))
        self.assertEqual([0, -1], nouvelle_orientation([1, 0], [1, 0], [[1, 0]]))
        self.assertEqual([1, 0], nouvelle_orientation([1, 0], [0, 1], [[1, 0]]))

unittest.main()
