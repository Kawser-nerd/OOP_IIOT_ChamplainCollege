from abc import ABC, abstractmethod

'''
ABC is abstract class
this will help us to define an abstract class in Python
'''
class Area(ABC):
    @abstractmethod
    def get_area(self):
        pass
    @abstractmethod
    def print_info(self):
        pass

class Rectangle(Area):
    def __init__(self, width, length):
        self.__width = width
        self.__length = length
    def get_area(self):
        return self.__width * self.__length
    def print_info(self):
        print("The Rectangle area ", self.get_area())

class Triangle(Area):
    def __init__(self, length, height):
        self.__length = length
        self.__height = height
    def get_area(self):
        return 0.5 * self.__length * self.__height
    def print_info(self):
        print("The Circle area: ", self.get_area())

class Square(Area):
    def __init__(self, length):
        self.__length =length
    def get_area(self):
        return pow(self.__length,2)
    def print_info(self):
        print("The Square area ", self.get_area())

if __name__ == '__main__':
    r1 = Rectangle(5,6)
    r1.print_info()

    tri = Triangle(10, 5)
    tri.print_info()

    s1 = Square(5)
    s1.print_info()
