import pyfirmata
import time

board = pyfirmata.Arduino('COM8')
# led = board.digital[12]
# button = board.digital[13]
led = board.get_pin('d:12:o')
button = board.get_pin('d:13:i')
previous_button_state = False
# start iteration
it = pyfirmata.util.Iterator(board)
it.start()

#button.mode = pyfirmata.INPUT

while True:
    time.sleep(0.1)
    button_state = button.read()
    print(button_state)
    #if button_state != previous_button_state:
    if button_state == 0:
        led.write(0)
    elif button_state == 1:
        led.write(1)
    #previous_button_state = button_state

