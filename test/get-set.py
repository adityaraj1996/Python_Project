class Employee:
    pass

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.mail = '{}-{}@email.com'.format(self.first, self.last)
    #     handling second explicit set part


    @property
    def fullname(self):
        return self.first + ' ' + self.last
    # setter method
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last


    # use setter method which will allow us to use defined method as an attribute only
    @property
    def mail(self):
        return self.first + '-' + self.last + '@email.com'


emp_1 = Employee('aditya', 'raj')
# explicit set
emp_1.first = 'ariyank'
emp_1.fullname = 'correy Schafer'
# this will change
print(emp_1.first)
# this will change
# print(emp_1.fullname())
# for setter
print(emp_1.fullname)
# this will not..for changing this we need to make email a method,
# but we will use setter method which will allow us to use defined method as an attribute only
print(emp_1.mail)