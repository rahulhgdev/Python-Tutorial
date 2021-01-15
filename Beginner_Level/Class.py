class Human:
    def __init__(self, n, o):
        self.name = n
        self.occupation = o

    def do_work(self):
        if self.occupation == "Tennis Player":
            print(self.name,"plays tennis")
        elif self.occupation == "Cricket Player":
            print(self.name,"Plays Cricket")

    def speak(self):
        print(self.name,"\nsay how are you?")

sachin = Human("Sachin Tendulkar","Cricker")
sachin.do_work()
sachin.speak()

print('\n')

maria = Human("Maria sharapova","Tennis")
sachin.do_work()
sachin.speak()

print('\n')


# built-in class modules

class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)
