import unittest
import unitfile





class TestCalc(unittest.TestCase):

    def setUp(self):
        self.a=10
        self.b=20

    def test_add(self):
        result= unitfile.sum(self.a , self.b)
        self.assertEqual(result,30)
        print(result)
    
    def test_multiply(self):
        result=unitfile.multiply(self.a,self.b)
        self.assertEqual(result,200)
        print(result) 

    def test_subtraction(self):
        result=unitfile.subtraction(self.a,self.b)
        self.assertTrue(result,10)
        print(result)

    def test_division(self):
        result=unitfile.division(self.a,self.b)
        self.assertTrue(result,2)
        print(result)

     

if __name__ == '__main__':
    unittest.main()

