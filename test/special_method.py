class Employee:
    pass

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

#special method (refer feb 7 on diary for theory)
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{}-{}'.format(self.full_name(), self.mail_id())

    def full_name(self):
        return self.first + ' ' + self.last




    def mail_id(self):
       return self.first + '_' + self.last + '@optum.com'


emp_1 = Employee('Alka', 'Jha', 50000)
emp_2 = Employee('Ariyank', 'Raj', 40000)
# background is print(emp_1.__repr__())
print(emp_2.__str__())
print(emp_2.mail_id())
