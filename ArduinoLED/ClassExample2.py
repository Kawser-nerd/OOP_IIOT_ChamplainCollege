# get the class from another module along with the methods
# import statements are usually used to call the libraies/predefine classes/library classes in the current module
import os
import serial
import ClassExample
''' If I want a specific class or method from a Module'''
from ClassExample import GradeCalculation, exampleMethod



# Create The class
class GradeLetterCalculation:
    def __init__(self, name, id, marks):
        self.__name = name
        self.__id = id
        self.__marks = marks
        '''
        If we just declare the variable inside the method, those variables are going to work as local variable.
        Those local variables are not supposed to share the values in between the class members, only will work
        inside the method.
        to make the variable as class variable inside the __init__() method, we need to use self keyword with 
        each of the variables 
        '''
    def _letterGrade(self):
        if(0<= self.__marks < 60):
            return 'F'
        elif(60<=self.__marks <=100):
            if (60 <= self.__marks <70):
                return 'D'
            elif (70<=self.__marks <80):
                return 'C'
            elif(80<=self.__marks <90):
                return 'B'
            else:
                return 'A'
        else:
            return "Please enter number in between 0 to 100"

    def _print_Student_Info(self):
        print("Student Name: ", self.__name, "\nStudent ID: " , self.__id, "\nStudent Marks:"
              , self.__marks, "\nStudent Letter Grade:" , self._letterGrade())

def input_Student_info():
    name = str(input("Enter Student Name: "))
    id = int(input("Enter Student Id"))
    marks = float(input("Enter Student Marks"))
    return name, id, marks


if __name__ == '__main__':
    '''
    1st Object/Instance
    '''
    name, id, marks = input_Student_info() # this will sequentially return three values, one after another to
    # your program, where the method called and will sequentially place the values to the left side variables
    student1 = GradeLetterCalculation(name=name, id=id, marks=marks) # name left is the keyword, put in the init method
    student1._print_Student_Info()

    # to invoke any Class from another Python Module, we need to create instance/Object of that class\
    ClassExample.GradeCalculation().print_Student_Info()
    ClassExample.exampleMethod()
    '''
    By default, Python Methods are static, means they always hold the last value in the variables and methods. So, you
    can call them directly without creating an object or instance, you can access each methods and attributes using
    the classname()
    '''




