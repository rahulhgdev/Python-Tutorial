

from polygon import Polygon

class Rectangle(Polygon):
    def area(self):
        return self.get_width() * self.get_height()
