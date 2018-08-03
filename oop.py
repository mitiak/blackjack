#!/usr/bin/python3

class Employee:

    raise_amount = 1.04
    num_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first.lower() + '.' + last.lower() + '@company.com'
        self.pay = pay

        Employee.num_of_employees += 1

    def __del__(self):
        Employee.num_of_employees -= 1
    
    def fullname(self):
        return('{} {}'.format(self.first, self.last))
    
    def apply_raise(self):
        self.pay = int((float)(self.pay) * self.raise_amount)

    #Class Method
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    #Alernative constructor
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    #static method
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} - {}".format(self.first, self.last)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


class Developer(Employee):
    raise_amount = 1.5
    def __init__(self, first, last, pay, prog_lang):

        #Call parent's constructpr - #1 - Use super()
        super().__init__(first, last, pay)

        #Call parent's constructpr - #2
        #Employee.__init__(self, first, last, pay)

        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self):
        for emp in self.employees:
            print('--->' + emp.fullname())


'''
Property decorator
'''

class Human:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split()

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None
        print('Name deleted')

hum = Human('Test', 'User')
print(hum.fullname)
print(hum.email)

hum.first = 'Jim'
print(hum.fullname)
print(hum.email)

#Set via fullname
hum.fullname = 'Dima Kovalchuk'
print(hum.fullname)
print(hum.email)

del hum.fullname
print(hum.fullname)
print(hum.email)


'''
Special methods
'''
# emp1 = Employee('Test', 'User', 10000)
# emp2 = Employee('Dima', 'Kovalchuk', 20000)
# print(emp1)

# print(repr(emp1))
# print(str(emp1))

# print(emp1.__repr__())
# print(emp1.__str__())

# print(emp1+emp2)

# print(len(emp1))


'''
isinstance, issubclass
'''
# dev1 = Developer('Test', 'User', '10000', 'python')
# dev2 = Developer('Dima', 'Kovalchuk', '20000', 'java')

# mgr1 = Manager('Gil', 'Shwed', 99999, [dev1])
# print(isinstance(mgr1, Manager)) #true
# print(isinstance(mgr1, Employee)) #true
# print(isinstance(mgr1, Developer)) #false

# print(issubclass(Developer, Employee)) #true
# print(issubclass(Manager, Employee)) #true
# print(issubclass(Developer, Manager)) #false


'''
Creating manager and modifying its employees
'''
# dev1 = Developer('Test', 'User', '10000', 'python')
# dev2 = Developer('Dima', 'Kovalchuk', '20000', 'java')

# mgr1 = Manager('Gil', 'Shwed', 99999, [dev1])
# print(mgr1.email)
# mgr1.print_emps()

# mgr1.add_employee(dev2)
# print(mgr1.email)
# mgr1.print_emps()

# mgr1.remove_emp(dev1)
# print(mgr1.email)
# mgr1.print_emps()

'''
Creating developers
'''
# dev1 = Developer('Test', 'User', '10000', 'python')
# print(dev1.email)
# print(dev1.prog_lang)


# dev2 = Developer('Dima', 'Kovalchuk', '20000', 'java')
# print(dev2.email)

'''
Method resolution
'''
# dev1 = Developer('Test', 'User', '10000')
# print(dev1.pay)
# dev1.apply_raise() # uses Developer raise_amount
# print(dev1.pay)
# dev2 = Developer('Dima', 'Kovalchuk', '20000')
# print(dev2.email)



'''
Alternative Constructor using class method
'''
# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Zohar-Mendelevich-80000'
# emp_str_3 = 'Shmuel-Goldklang-80000'

# first, last, pay = emp_str_1.split('-')
# new_emp1 = Employee(first, last, pay)
# print(new_emp1.fullname())

# new_emp2 = Employee.from_string(emp_str_2)
# print(new_emp2.fullname())

# print('emp1.fullname():' + emp1.fullname())
# print('Employee.fullname(emp1):' + Employee.fullname(emp1))

'''
Class Variables and methods
'''
# print(emp1.__dict__)
# emp1.raise_amount=1.05
# print(emp1.__dict__)
# print(Employee.raise_amount)
# print(emp1.raise_amount)
# print(emp2.raise_amount)

# Employee.raise_amount=1.05
# Employee.set_raise_amt(1.05)
# print(Employee.raise_amount)
# print(emp1.raise_amount)
# print(emp2.raise_amount)





