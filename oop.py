#!/usr/bin/python3

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first.lower() + '.' + last.lower() + '@company.com'
        self.pay = pay
    
    def fullname(self):
        return('{} {}'.format(self.first, self.last))

emp1 = Employee('Test', 'User', '10000')

print('emp1.fullname():' + emp1.fullname())
print('Employee.fullname(emp1):' + Employee.fullname(emp1))






