import unittest

def sum(a,b):
    return a + b
 
class SumRams(unittest.TestCase):
    def test_sum(self):
        a=10
        b=10


        result=sum(a,b)
        print(result)
       # c == result
        self.assertEqual (a,b)
       # def test_issum(self):
        #    self.assertTrue(a==b.issum())

       # print(a+b)
        #c=a+b

        #if(c == 20 ):
        #    print("Equal to")

        #else:
         #   print("No")

            
    
if __name__ == "__main__":
    unittest.main()

    