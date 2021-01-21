
from abc import ABC, abstractclassmethod          # abc - abstract base class & python don't provide any abstract class there is a built-in modules which is in this line


class Shape(ABC):
    @abstractclassmethod        # its decorator
    def area(self): pass        # empty method

    #@abstractclassmethod          # abstractmethod is a mthd which must be implemented in subclass
    def perimeter(self):pass

class Square(Shape):
    def __init__(self, side):
        self.__side = side
    def area(self):
        return self.__side * self.__side
    def perimeter(self):
        return 4 * self.__side


square = Square(5)    # it can't be intantiated bcoz its abstract class
print(square.area())
print(square.perimeter())