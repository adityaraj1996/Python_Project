class employee:
    pass
# this is the example for creating instances and attributes and manually creating the entries
 #   def__init__(self,first,last,pay):
  #  self.first = first
emp_1 = employee()     # unique instance of class
emp_2 = employee()      # unique instance of class
print(emp_1)
print(emp_2)
emp_1.first = 'Aditya'     # attributes for the instances unique to the instance
emp_1.last = 'Raj'
emp_1.pay = 30000
emp_1.mail = emp_1.first + emp_1.last + '@optum.com'

emp_2.first = 'Abhishek'
emp_2.last = 'Mandal'
emp_2.pay = 35000
emp_2.mail = emp_2.first + emp_2.last  + '@optum.com'
print(emp_2.mail)
print(emp_1.first)