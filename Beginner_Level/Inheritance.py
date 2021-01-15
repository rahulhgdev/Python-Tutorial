class Vehicle:
    def genral_usage(self):
        print("use for transportation")

class Car(Vehicle):
    def __init__(self):
        print("I'm a car")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        self.genral_usage()
        print("specific usage: commute to work, vacation with family")

class Motorcycle(Vehicle):
    def __init__(self):
        print("I'm a Motorcycle")
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        self.genral_usage()
        print("specific usage: road trip, racing")

c = Car()
#c.genral_usage()   # if you don't want to call general_usage() explicitly, you can call inside class as above
c.specific_usage()
print('\n')
m = Motorcycle()
#m.genral_usage()
m.specific_usage()

print('\n')

print(isinstance(c,Car))               # check and return bool value
print(isinstance(c,Motorcycle))

print('\n')

# another example

class Parent:        # define parent class
   parentAttr = 100
   def __init__(self):
      print("Calling parent constructor")

   def parentMethod(self):
      print('Calling parent method')

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print("Parent attribute :", Parent.parentAttr)

class Child(Parent): # define child class
   def __init__(self):
      print("Calling child constructor")

   def childMethod(self):
      print('Calling child method')

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method

print('\n')

# method overriding

class Parent:        # define parent class
   def myMethod(self):
      print('Calling parent method')

class Child(Parent): # define child class
   def myMethod(self):
      print('Calling child method')

c = Child()          # instance of child
c.myMethod()         # child calls overridden method

print('\n')

# Multiple Inheritance

class Father:
    def skills(self):
        print("Gardening & Programming")

class Mother:
    def skills(self):
        print("cooking & art")

class child(Father,Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("sports & gaming")

c = child()
c.skills()

