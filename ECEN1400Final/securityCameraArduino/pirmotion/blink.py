import pyfirmata

board = pyfirmata.Arduino("/dev/ttyUSB0")

while True:
    board.digital[9].write(1)
    board.pass_time(1)
    board.digital[9].write(0)
    board.pass_time(1)