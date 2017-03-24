import unittest
from lags import *

class LagsTest(unittest.TestCase):
    def setUp(self):
        self.fly_list = [["AF514", 0, 5, 10], 
            ["CO5", 3, 7, 14], 
            ["AF515", 5, 9, 7], 
            ["BA01", 6, 9, 8]]

    def test_check_fly(self):
        self.assertEqual(True, check_flys(self.fly_list))

    def test_check_gain_max(self):
        self.assertEqual(14, check_gain_max(self.fly_list))

    def test_check_hours(self):
        self.assertEqual([[0, 5],[3, 10], [5, 14], [6, 15]], check_hours(self.fly_list))

    def test_check_compatibility(self):
        self.assertEqual([[0, 2], [0, 3]], check_compatibility(self.fly_list))



unittest.main()
