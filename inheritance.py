class employee: #create a class
     
     def employee_name(self):
        self.name1="ramalingam"
        self.name="gowtham"
        print("employee name is:",self.name1)
        print("employee name is:",self.name)

class employee1:
    
    def employee_salary(self):#create funcion with default argument
        self.ram=10000
        self.yuvan=10000
        print("salary ram=",self.ram)
        print("salary yuvan=",self.yuvan)

class employee2(employee):   #create a child class

    def employee_allowance(self):
        self.allowance=2000
        print("employee allowanc=",self.allowance)

class employee3(employee2): #create a child 2 class
     
    def employee_designation(self):
        self.designation="manager"
        print("emploee designation=",self.designation) 

e1=employee3()
e1.employee_name()
e1.employee_designation()
e1.employee_salary()
e1.employee_allowance()


