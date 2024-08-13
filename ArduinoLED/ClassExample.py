'''
Create Class GradeCalculation, with Marks and Name input and do the calculation. Also input the Student ID
'''

class GradeCalculation: # Camel Case
    ''' Class name followed by semicolon
     Global Class Variables: These variable are used to be inside the class scope, not outside'''
     # global variable
    std_name = ""
    std_ID = 0
    std_Grade = 0

    def input_Student_Info(self):

        ''' Input Student
        
        Inside each method, the self variable passes the default value of the class variables and allow us
        to call the values with variables whenever required. By default, the self parameter passes all the 
        class global variables along with all the class methods and attributes
        
        for this method, self is holding the num, std_name, and std_ID variables
        '''
        name = str(input("Enter Student Name"))
        self.set_Student_Name(name=name)
        ID = int(input("Enter Student ID"))
        self.set_Student_ID(ID=ID)
        grade = self.input_Grade() # whenever we will call any class method inside the class, we shoul
        self.set_Student_Grade(grade=grade)

    def input_Grade(self): # Class Method
        grade = float(input("Enter Student Grade"))

        return grade

    ''' Accessor Methods'''
    def set_Student_Name(self, name):
        self.std_name = name

    def set_Student_ID(self, ID):
        self.std_ID = ID

    def set_Student_Grade(self, grade):
        self.std_Grade = grade

    ''' Mutator Methods: Get Methods 
    In Python, most of the programs do not use mutators method... the reason is you are using the class global 
    variables, so you can call them directly with self keyword, you don't need to call the methods to get them
    '''
    def get_Student_Name(self):
        return self.std_name

    def get_Student_LetterGrade(self):
        if(self.std_Grade < 60):
            return 'F'
        else:
            if(60 <= self.std_Grade <70):
                return 'D'
            elif(70 <= self.std_Grade <80):
                return 'C'
            elif(80 <= self.std_Grade <90):
                return 'B'
            elif(90 <= self.std_Grade <= 100):
                return 'A'
            else:
                return "Please enter valid number between 0 to 100"

    def print_Student_Info(self):
        print("Student name : ", self.std_name, ", \n student ID : ", self.std_ID, ",\n Grade : ", self.std_Grade
              , ", \n Student Letter Grade ", self.get_Student_LetterGrade())

def exampleMethod():
    print("Outside Class Method")
'''
Python doesn't have a default main program. You don't need to create a main program as well. Python, by default
start execution from the first line and then it executes line by line
if you want to control the entry point of the program by yourself, (custom entry point), you should use the
following line. This wll start the python compiler to compile your from  the following line and then, based on the
sequence you will ask the program to follow, compiler will follow that path. 
'''
if __name__ == '__main__':
    # Create 1st Object of GradeCalculation Class
    '''
    we need to create a variable on the left side of the assignment operator and then Call the ClassName with 
    parantheses on the right side of the assignment operator. This will create first instance//clone of the class
    in the left side variable
    the reason of the parantheses is to send default values to the class parameter whenever required
    '''
    '''1st Instance'''
    studentOne = GradeCalculation()
    studentOne.input_Student_Info() # This will call the method present inside the class
    studentOne.print_Student_Info()
    ''' 2nd Instance'''
    studentTwo = GradeCalculation()
    studentTwo.input_Student_Info()
    studentTwo.print_Student_Info()

