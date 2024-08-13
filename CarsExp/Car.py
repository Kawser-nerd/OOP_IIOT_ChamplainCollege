'''
In this program, we are going to create a car class, that is going to hold the car name, model, year and color.
User proper accessors and mutators, as the user to give input the name, model, year and color and print them back
to the output window
'''

class CarDetails:
    def __init__(self, name, model):
        self.name = name
        self.model =model
        self.year = 0
        self.color = ""

    # Mutators
    def set_Year(self, year):
        self.year = year

    def set_Color(self, color):
        self.color = color

    # Accessors
    def get_Name(self):
        return self.name

    def get_Model(self):
        return self.model

    def get_Year(self):
        return self.year

    def get_Color(self):
        return self.color

    # We are going to print the values we want the class to print
    def print_details(self):
        print("Name: " + self.get_Name() , "\nModel: " + self.get_Model() , "\nYear: " + self.get_Year()
              , "\nColor: " + self.get_Color()) # Encapsulation

    def __str__(self): # this method will get invoked when user wants to print the object been created from the class
        return ("Name: " + self.get_Name() +
                "\nModel: " + self.get_Model() +
                "\nYear: " + self.get_Year() +
                "\nColor: " + self.get_Color())

    def __repr__(self): return ("Name: " + self.get_Name())

def input_car_name():
    carName = input("What is your car name? ")
    return carName

def input_car_model():
    carModel = input("What is your car model?")
    return carModel

def input_car_year():
    carYear = input("What is your car year?")
    return carYear

def input_car_color():
    carColor = input("What is your car Color")
    return carColor

