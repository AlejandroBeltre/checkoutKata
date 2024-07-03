import unittest
from main import Checkout

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.rules = {
            'A': (50, (3, 130)),
            'B': (30, (2, 45)),
            'C': (20, None),
            'D': (15, None)
        }


    def test_totals(self):
        co = Checkout(self.rules)
        self.assertEqual(co.total(), 0)

    def test_totals_hasItem(self):
        co = Checkout(self.rules)
        co.scan('D')
        self.assertEqual(15, co.total())


    def test_totals_hasTwoItems(self):
        co = Checkout(self.rules)
        co.scan('D')
        co.scan('D')
        self.assertEqual(30, co.total())




if __name__ == '__main__':
    unittest.main()


# comment