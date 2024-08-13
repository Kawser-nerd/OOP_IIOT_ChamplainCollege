import datetime

'''
currentDateTime = datetime.datetime.now()
print(currentDateTime.__str__())
print(currentDateTime.__repr__())
'''

# read the contexts from the test.txt file
# default class to open a file in ... modes:
# i> read mode  --- r
# ii> write,  --- w
# iii> append, w+ /a
# iv> read with append,r+
# v> create if you don't have the file or read if it is already present
# by default, the open class opens the file in create

file = open('test.txt', 'r').readlines()
'''
readlines(): this method will read the file context with newlines
read(): this will read the file context without newlines, it will a single character at a time
'''

for line in file.readlines():
    print(line)

# for reading from a file, its not necessary to close the file, but for writing on the file, it is mandatory because
    # python puts everything in buffer and only write the buffer to file when you closed it.
file.close()

# Another structure
with open('test.txt', 'r') as file:
    for line in file.readlines():
        print(line)