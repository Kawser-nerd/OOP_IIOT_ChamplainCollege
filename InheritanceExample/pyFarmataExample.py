import pyfirmata
import time # it will make some delay

board = pyfirmata.Arduino('COM8') # port number where your arduino is connected
# ledPin = board.get_pin('d:12:o') # we need to provide three information: digital/analog, pinno, input/output
# button = board.get_pin('d:13:i')
ledPin = board.digital[12]
button = board.digital[13]

# start board iteration
it = pyfirmata.util.Iterator(board)
it.start()

while True:
    time.sleep(0.1)
    button_state = button.read()
    print(button_state)
    if button_state == True:
        ledPin.write(1)
    elif button_state == False:
        ledPin.write(0)

