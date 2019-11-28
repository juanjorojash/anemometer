import time
import serial


ser = serial.Serial(
  
    port='/dev/ttyS0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)
counter=0
clear=b'\xFE\x01'
ser.write(clear)
while 1:
    ser.write(clear)
    ser.write(('Write counter:  %d'%(counter)).encode('utf-8'))
    time.sleep(1)
    counter += 1
