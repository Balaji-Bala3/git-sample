class Employee():
    def emp_Id(self):
        print("Employee ID is 123")
    def emp_Name(self):
        print(id(self))
        print("Employee name is Raj")
    def emp_Dob(self):
        print("Employee Dob is 12/3/95")
        print(id(self))
    def emp_Phone(self):
        print("Employee phone no is 123")
    def emp_Email(self):
        print("Employee mail ID is 123@gmail.com")
    def emp_Address(self):
        print("Employee adsress is 123 north street, Chennai")
e=Employee()
e.emp_Id()
e.emp_Name()
e.emp_Dob()
e.emp_Phone()
e.emp_Email()
e.emp_Address()
print(id(e))
m=Employee()
m.emp_Address()
print(id(m))