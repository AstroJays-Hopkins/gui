import serial
import struct
import sys

ser = serial.Serial(port='/dev/cu.usbmodem14301')
while(ser.isOpen()):
    header = ser.read(1)
    if header == b'U':
        buffer = ser.read(15)
        print(buffer)
        print(sys.getsizeof(buffer))
        received = struct.unpack('=fcfcfc',buffer)
        print(received)      
        
    else:
        print("failed")
    
    