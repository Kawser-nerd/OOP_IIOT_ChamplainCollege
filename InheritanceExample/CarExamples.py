# First Class: Automobile Class

class Automobile: # SuperClass
    def __init__(self, make, model, mileage, price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def set_price(self, price):
        self.__price = price

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_mileage(self):
        return self.__mileage

    def get_price(self):
        return self.__price

    def __str__(self):
        return (f'The car manufacturer is  {self.get_make()} model is  {self.get_model()} mileage is '
                f' {self.get_mileage()} price is  {self.get_price()}')

class Car(Automobile):
    def __init__(self,make, model, mileage, price, no_of_doors):
        super().__init__(make=make, model=model, mileage=mileage, price=price) # this is calling the super class init method, automobile class
        '''
        whenever you are inheriting a class and if that class has a init(), then, in the derived class, you definitely
        need to initialize the parent class/super class init method with the appropriate arguments. That means, you 
        need to pass the values for all the arguments you designed for the parent class
        
        In this example, Automobile class is going to init for arguments: make, model, mileage and price. You need to 
        initialize the the automobile class init method and pass the the arguments value. So, you need to take all the
        super class init method arguments in your derived class argument list. And when you create the object of the
        derived class, you will pass not only the derived class arguments but also the super class arguments.
        '''
        self.__no_of_doors = no_of_doors

    def set_no_of_doors(self, no_of_doors):
        self.__no_of_doors = no_of_doors

    def get_no_of_doors(self):
        return self.__no_of_doors

    def __str__(self):
        return (f'The make of the car is {self.get_make()} and the model of the car is {self.get_model()} the mileage is {self.get_mileage()}'
                f' and the price is {self.get_price()}, the number of doors is {self.get_no_of_doors()}')

class SUV(Automobile):
    def __init__(self, make, model, mileage, price, passenger_capacity):
        super().__init__(make=make, model=model, mileage=mileage, price=price)
        self.__passenger_capacity = passenger_capacity

    def set_passenger_capacity(self, passenger_capacity):
        self.__passenger_capacity = passenger_capacity

    def get_passenger_capacity(self):
        return self.__passenger_capacity

    def __str__(self):
        return (f'The make of the SUV is {self.get_make()} and the model of the car is {self.get_model()} the mileage is {self.get_mileage()}'
                f' and the price is {self.get_price()} and the passenger_capacity is {self.get_passenger_capacity()}')

class Truck(Automobile):
    def __init__(self, make, model, mileage, price, drive_type):
        super().__init__(make=make, model=model, mileage=mileage, price=price)
        self.__drive_type = drive_type

    def set_drive_type(self, drive_type):
        self.__drive_type = drive_type

    def get_drive_type(self):
        return self.__drive_type

    def __str__(self):
        return (f'The make of the Truck is {self.get_make()} and the model of the car is {self.get_model()} the mileage is {self.get_mileage()}'
                f' and the price is {self.get_price()} and the drive type is {self.get_drive_type()}')

if __name__ == '__main__':
    car1 = Car('Toyato', 'Camry', 127500, 12000, 4)
    car2 = Car('Ford', 'Torus', 210000, 7000, 4)

    suv1 = SUV('Toyato', 'Rav4', 85000, 15000, 5)
    suv2 = SUV('Ford', 'Flex', 145897, 18000, 8)

    truck1 = Truck('Nissan', 'Tundra', 227500, 7500, '4 X 4')
    truck2 = Truck('Ford', 'F150', 21478, price=50200, drive_type='AWD')

    auto1 = Automobile('Honda', 'VFR', 16000, 12000)

    print(car1)
    print(car2)
    print(suv1)
    print(suv2)
    print(truck1)
    print(truck2)
    print(auto1)


