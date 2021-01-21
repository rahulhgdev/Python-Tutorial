
# COMPOSITION HAS relation of 'PART - OF ' #
# AGGREGATION HAS relation of 'HAS - A'  #

class Salary:

    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return (self.pay*12) + self.bonus

class Employee:
    def __init__(self, name, age , salary):
        self.name= name
        self.age= age
        self.obj_salary = salary;

    def total_salary(self):
        return   self.obj_salary.annual_salary()


salary = Salary(15000, 10000)
emp = Employee('easynamila', 25, salary)           # Its unidirectional only salary is passing not name and age     # don't forget to pass salary object

print(emp.total_salary())