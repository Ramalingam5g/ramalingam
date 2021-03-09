import unittest
import Employee
class TestEmployee(unittest.TestCase):
    def name_test(self):
        emp_1=Employee("ram","manager")
        emp_2=Employee("sam","trainer")

        self.assertEqual(emp_1.name,"ram") 
        self.assertEqual(emp_2.name,"sam")

        emp_2.name="ram"

        self.assertEqual(emp_2.name,"ram")

      
    def designation_test(self):
        emp_1=Employee("ram","manager")
        emp_2=Employee("sam","trainer")

        self.assertEqual(emp_1.designation,"manager")
        self.assertEqual(emp_2.designation,"trainer")

        emp_1.designation="trainer"

        self.assertEqual(emp_1.designation,"trainer")

if __name__ == "__main__":
    unittest.main()