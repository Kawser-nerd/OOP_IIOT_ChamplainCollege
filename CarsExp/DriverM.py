'''
This module will contain the main accessing details of the program, means main method !!!
'''

from Car import input_car_name, input_car_model
# from Car import input_car_year, input_car_color
# from Car import * means all
import Car # all us the references of all the class and methods


if __name__ == '__main__':
    # take input from the users
    carY = Car.input_car_year()
    carC = Car.input_car_color()
    carN = input_car_name()
    carM = input_car_model()


    # access the Class members with object
    # each object holds a single car information
    firstCar = Car.CarDetails(name=carN, model=carM) # __init__(self) method value passing
    firstCar.set_Year(carY)
    firstCar.set_Color(carC)

    print("Car Name : ", firstCar.get_Name())
    print("Car Model : ", firstCar.get_Model())
    # print everything
    print(firstCar.print_details())

    # print the object
    print(firstCar)
