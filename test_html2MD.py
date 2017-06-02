import unittest
from html2MD import *

class TestMarkDown(unittest.TestCase):
    def test_h1(self):
        self.assertEqual("# je suis une loutre\n", extract("<h1>je suis une loutre</h1>"))

    def test_p(self):
        self.assertEqual("je suis une loutre\n", extract("<p>je suis une loutre</p>"))

    def test_h3(self):
        self.assertEqual("### je suis une loutre\n", extract("<h3>je suis une loutre</h3>"))


if __name__ == "__main__":
    unittest.main()
