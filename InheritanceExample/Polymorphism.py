class Area:
    def __init__(self, length, width, height):
        self.__length = length
        self.__width = width
        self.__height = height

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width
    def get_height(self):
        return self.__height
    def get_area(self):
        return self.__length * self.__width * self.__height

    def print_info(self):
        print('Area ', self.get_area())

class Rectangle(Area):
    def __init__(self, length, width, height):
        super().__init__(length, width, height)

    def get_area(self):
        return self.get_width() * self.get_length()

    def print_info(self):
        print('The area of Rectangle ', self.get_area())

class Square(Area):
    def get_area(self):
        return self.get_length() * self.get_length()

    def print_info(self):
        print('The area sqaure', self.get_area())

class Triangle(Area):
    def get_area(self):
        return 0.5 * self.get_length() * self.get_height()

    def print_info(self):
        print( 'The area triangle', self.get_area())


area = Area(2,5,6)
area.print_info()
square = Square(2,5,6)
square.print_info()

rec = Rectangle(2, 4, 3)
rec.print_info()
