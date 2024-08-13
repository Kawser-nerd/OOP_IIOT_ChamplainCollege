import serial.tools.list_ports# this library will help us to load all the available port

ports = serial.tools.list_ports.comports()# reading all the open ports to my ports array
serialInst = serial.Serial()
portList = []
for port in ports:
    portList.append(str(port))
    print(str(port)) # to get the port number correctly

com = input("Select the Arduino Port #")
for i in range(0,len(portList)):
    if portList[i].startswith("COM" + str(com)):
        use = "COM" + str(com)
        print(use)

# Arduino Communication
serialInst.baudrate = 9600
serialInst.port = use
serialInst.open()

while True:
    command = input("Enter command ON/OFF/QUIT")
    serialInst.write(command.encode('utf-8'))
    serialInst.flush()

    if command == "QUIT":
        exit(1)

