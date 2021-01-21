
class Parent:
    def __init__(self, name):
         print('Parent __init__', name)


class Parent2:
    def __init__(self, name):
         print('Parent2 __init__', name)

class Child(Parent, Parent2):
    def __init__(self):
        print('Child __init__')
        super().__init__('chamn')                    # to call the __init__ of superclas
      #  Parent.__init__(self, 'ram')
      #  Parent2.__init__(self, 'max')

child = Child()
print(Child.__mro__)                   # mro method resoution order. After running u can see that 1st method of child class executed then parents class method


