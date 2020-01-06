class Employee:
    #class variable
    no_of_emp = 0
#here __init__() is the initialise method and self is the instance same as emp_1 and is automatically passed arg

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.no_of_emp += 1




emp_1 = Employee('aditya','raj',30000)
emp_2 = Employee('ariyank','raj',40000)
#print(emp_1)
#print(emp_2)
'''
emp_1.first = 'Aditya'     # attributes for the instances unique to the instance
emp_1.last = 'Raj'
emp_1.pay = 30000
emp_1.mail = emp_1.first + emp_1.last + '@optum.com'

emp_2.first = 'Abhishek'
emp_2.last = 'Mandal'
emp_2.pay = 35000
emp_2.mail = emp_2.first + emp_2.last  + '@optum.com'
'''
print(emp_2.pay)
# same as print(emp_1.mail()) ---no need to pass the instance but background is lyk this only
#print(Employee.mail(emp_1))
print(emp_1.first)
print(Employee.no_of_emp)