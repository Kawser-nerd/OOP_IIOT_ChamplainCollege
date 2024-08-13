'''
print('Hello ArduinoLED')
print("Hello ArduinoLED")
print("Hello ArduinoLED ", "Example Class")

num = 20

# print("Hello ArduinoLED ", num)

string1 = 'Hello Nafi '

print(string1, num)

# Single Line Comment


Multi-Line Comment
Multile Comment Block



x = int(10.25) # Represents Integer conversion/ Integer numbers
print(x)
Y = float(10.25)
print(Y)
Zo = str('Value')
print(Zo)


num1 = float(input('Enter Some Number')) # This will allow us to open the port and take input from the user
num2 = float(input('Enter Some Number')) # This will allow us to open the port and take input from the user
#result = num1 % num2
result = num1 ** num2
print(result)


print('Hello Welcome')
print('Hello ArduinoLED \n') # Its newline
print('Hello\tNafi') # will put double space in between the strings

num = 10

print('The number I put is ', num, ' and this is going to be final')
print(f'The number I put is {num * num} and this is going to be final') # print is the function and f inside is formatter

num2 = 12.5698765
print(f'{num2:>20.2f}')

NUM3 = 120 # as python doesn't support constant number, you can use Captial Literals for all the variable name and we can reuse it


num1 = int(input('Enter Some Number'))
num2 = int(input('Enter Some Number'))

choice = int(input('Enter your choice: 1 for addition \n, 2 for multiplication \n, 3 for subtraction,\n 4 for division'))

if choice == 1: # individual single condition
    print(num1 + num2)
elif choice == 2: # individual 2nd single condition
    print(num1 * num2)
elif choice == 3:
    print(num1 - num2)
elif choice == 4:
    print(num1 / num2)
else:
    print('Invalid Choice, Enter Proper choice')
'''
# import random

# Letter Grade Conversion
'''

90 =< Marks ---> A*
90 > Marks>= 80 ---> A
80 > Marks>= 70 ---> B
70 > Marks>= 60 ---> C
60 < ---> F


marks = float(input('Enter Marks: '))
if marks < 60:
    print('Grade: F')
else:
    if 60 <= marks < 70:
        print('Grade: C')
    elif marks >= 70 and marks<80:
        print('Grade: B')
    elif marks >=80 and marks<90:
        print('Grade: A')
    else:
        print('Grade: A*')


var1 = 20
var2 = 36
if not (var1 < 15 and var2 < 30):
    print("successful")


if(area := (width:=25) * (height :=30))> 200:
    print(area)


temperature = random.randint(10, 50) # this will randomly generate a number in between 10 to 50
print(temperature)
while temperature >= 20:
    print("Hot weather temperature is: ", temperature)
    temperature = random.randint(10, 50)
    print(temperature)



make this program work in a different way

while True:
    temperature = random.randint(10, 50)
    print(temperature)
    
    if temperature >= 20:
        print("Hot weather temperature is: ", temperature)
    else:
        print("Not enough hot")
        break
    
    if temperature < 20:
        print("Not hot temperature ", temperature)
        break
    print("Hot weather temperature is: ", temperature)
'''
# limit provided for loop
# for loop requires 3 information.. initializer, upper limit, increment value/ stepping value
# for i in range(10): # this means upper limit is 10, lower limit by default 0, increment by default 1
#    print(i)
# for i in range(3,10): # this means, initializer is 3, upper limit 10, increment by default 1
#    print(i)

# for i in range(2, 10, 2): # this means, initializer is 2, upper limit is 10, increment by 2 steps
#    print(i)

# arr = [2, 3, 4, 6, 8, 9] # array
# for i in arr:
#    print(i)
# arr = {2,3,4,5,9,8} # list
# for i in arr:
#    print(i)


'''
Functions
'''

#def gradeCalculation(m, name): # m here works as a local variable, this will catch the value send from function call place
    # m, name here is the local parameter/variable, will used as keyword
    # m is a local variable
# to make sure your function is only going to take keyword based parameter/variable passing
#def gradeCalculation(*, m, name): # * at the beginning of the parameter list means you have to use keyword based value passing for all the variable next to *
# to make sure your function is only going to take positional sequence maintained values instead of keyword matching
import random
import os

num = 15 # Global Variable -- this variable is accessed by all the methods whenever required
def gradeCalculation(m, name, collegename="ChamplainCollege", institionNo=1257): # / means we are going to accept only positional sequnce values for the m and name variables, which are placed before the character
    print("Student name: ", name)
    print("College name: ", collegename) # college name is default argument
    print("Institution Number: ", institionNo) # institutionNo is default argument
    if m < 60:
        print("letter grade F")
    elif m >= 60:
        if 60<=m<70:
            print("letter grade C")
        elif 70<=m<80:
            print("letter grade B")
        elif 80<=m<90:
            print("letter grade A")
        else:
            print("letter grade A*")
    else:
        print("Invalid number")

name = str(input("Enter name: "))
marks = int(input("Enter marks: "))  # Global VALUE
# send the parameters with maintaining proper sequence
gradeCalculation(marks, name, "Ecole Polytechnique") # funciton call with positional order/sequence

# we can send parameters with keyword. Keywords mean the letters you used as variable in the function body. for our
# program, it is m and name, we can call the keywords and directly pass the variable to those variables/parameters/keywords
gradeCalculation(name=name, m=marks, collegename="Ecole Polytechnique", institionNo=25897)
