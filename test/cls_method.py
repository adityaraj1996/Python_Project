class Employee:
    # this is the class variable which will be shared by all the emp instances.
    raise_amt = 1.04
#here __init__() is the initialise method and self is the instance same as emp_1 and is automatically passed arg

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    def mail(self):
        return self.first + '_' + self.last + '@optum.com'
    # this is for the need to make this raise_amt a class variable
    def apply_raise(self):
        # this was without using calss variable
        #self.pay = int(self.pay * 1.04)
        # using class variable
        self.pay = int(self.pay * self.raise_amt)
  #  def apply_raise(self):
        self.pay = int(self.pay + self.raise_amt)
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
 # below static method will take in a date and return whether or not it was a working day
    @staticmethod
    def is_workday(day):
 # in python , we hve weekday method where monday == 0 and sunday ===6
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True



emp_1 = Employee('aditya', 'raj', 30000)
emp_2 = Employee('ariyank', 'raj', 40000)
import datetime
year, month, day = list(map(int, input('enter yyyy mm dd format').strip().split(' ')))
my_date = datetime.date(year, month, day)
print(Employee.is_workday(my_date))
emp_str_1 = 'aditya-raj-10000'
emp_str_2 = 'ariyank-raj-40000'
#Employee.set_raise_amt(1.05)
#first, last, pay = emp_str_1.split('-')  this is used when we don't use class method
#new_emp_1 = Employee(first, last, pay)
# below is using class method
new_emp_2 = Employee.from_string(emp_str_2)




print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)
print(emp_2.pay)
emp_2.apply_raise()
print(emp_2.pay)
print(new_emp_2.pay)

#print(emp_2.apply_raise())