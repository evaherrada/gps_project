import board
import busio


LOG_FILE = '/gps.txt'  # Example for writing to internal path /gps.txt

LOG_MODE = 'ab'

RX = board.RX
TX = board.TX

uart = busio.UART(TX, RX, baudrate=9600, timeout=30)

with open(LOG_FILE, LOG_MODE) as outfile:
    while True:
        sentence = uart.readline()
        print(str(sentence, 'ascii').strip())
        outfile.write(sentence)
        outfile.flush()

