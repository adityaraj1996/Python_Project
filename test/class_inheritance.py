class Employee:
    avg_hike = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def full_name(self):
        return self.first + ' ' + self.last

    def apply_hike(self):
        self.pay = int(self.pay * self.avg_hike)

    @classmethod
    def set_hike(cls, hike):
        cls.avg_hike = hike

class Developer(Employee):
    avg_hike = 1.10
    #soemtimes , our child class needs to handle more attributes than parent class in which case we redefine
    #the init method by adding the attirbute and using super() method to use the older attributes from parent class

    def __init__(self, first, last, pay, sex):
        super().__init__(first, last, pay)
        self.sex = sex

class Manager(Employee):

    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        # if emp in self.employees:
        #     print('==>' , emp.full_name())
        if self.employees is not None:
            for emp in self.employees:
                print('==>', emp.full_name())

emp_1 = Employee('Aditya', 'Raj', 30000)
emp_2 = Employee('khushi', 'Mishra', 4000)
emp_3 = Employee('Sakshi', 'sharma', 5000)
mgr_1 = Manager('ashish', 'jain', 10000,[emp_1])
mgr_2 = Manager('manish', 'grover', 10000,[emp_2, emp_3])
print(mgr_1.full_name())
mgr_2.remove_emp(emp_3)
mgr_2.print_emp()
mgr_2.add_emp(emp_3)
mgr_2.print_emp()
mgr_1.print_emp()
# inheritance used
#dev_1 = Employee('abhishek', 'mandal', 40000)
dev_1 = Developer('abhishek', 'mandal', 40000, 'male')
dev_1.apply_hike()
print(dev_1.full_name())
print(dev_1.sex)
print(dev_1.pay)
print(Employee.avg_hike)
emp_1.set_hike(2)
dev_1.set_hike(3)
print(emp_1.avg_hike)
emp_1.apply_hike()
# inheritance used
dev_1.apply_hike()
print(emp_1.pay)
print(dev_1.pay)
# this built in used to see whether an instance is an instance of a given class
print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Developer))
print(issubclass(Developer, Manager))
# help function is to find the method resolution order
# print(help(Developer))
# print(Developer.mro())