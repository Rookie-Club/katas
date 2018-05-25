import unittest
import diamond

class MyTest(unittest.TestCase):		
	def test_print_diamond_A(self):
		value = "A"
		value_expect = "A"
		result = diamond.print_diamond(value)
		self.assertEqual(result, value_expect)

	def test_print_diamond_B(self):
		value = "B"
		value_expect = "\n A \nB B\n A \n"
		result = diamond.print_diamond(value)
		self.assertEqual(result, value_expect)

unittest.main()