import unittest
import unitfile

class  TestAddition(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(unitfile.sum(10,3),13)
        self.assertEqual(unitfile.sum(10,-2),8)
        self.assertEqual(unitfile.sum(10,10),20)

    def test_multiply(self):
        self.assertEqual(unitfile.multiply(10,2),20)

    def test_division(self):
        self.assertEqual(unitfile.division(10,10),1)

    def test_isupper(self):
        self.assertFalse("FOO".islower())

    def test_islower(self):
        self.assertTrue("f00".islower())



if __name__ == "__main__":
    unittest.main()