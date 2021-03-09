class employee:
    def __init__(self):
        self.salary=10000
        self.designaion="softwaretrainee"
        self.company="fifthgentech"
        print("Employees details")

    def welcome(self):
        print("salary:",self.salary)
        print("designation:",self.designaion)
        print("company:",self.company)

e2=employee()
e2.welcome()


