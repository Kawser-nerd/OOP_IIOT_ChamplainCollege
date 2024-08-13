import serial.tools.list_ports

ports = serial.tools.list_ports.comports() # will get communication ports
serialInst = serial.Serial() # serial instance as we are going to communicate with serial port
portsList = []

for one in ports:
    portsList.append(str(one))
    print(str(one))

com = input("Select COM port for Arduino #: ")

for i in range(len(portsList)):
    if portsList[i].startswith("COM" + str(com)):
        use = "COM" + str(com)
        print(use)

serialInst.baudrate = 9600
serialInst.port = use
serialInst.open()

while True:
    command = input("Enter command: (ON/OFF/exit): ")
    serialInst.write(command.encode('utf-8'))
    serialInst.flush()


    if command == "exit":
        exit()

