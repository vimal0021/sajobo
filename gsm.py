import serial
import RPi.GPIO as GPIO      
import os, time, sys
 
GPIO.setmode(GPIO.BOARD)    
port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)
print("1")

 
port.write(b'AT+CMGF=1'+b'\r\n')  # Select Message format as Text mode 
rcv = port.read(10)
print (rcv)
time.sleep(1)
print("12") 
 
# Sending a message to a particular Number
 
port.write(b'AT+CMGS="9539297709"'+b'\r\n')
rcv = port.read(10)
print (rcv)
time.sleep(1)
 
port.write(b"Hello User"+b'\r\n')  # Message
rcv = port.read(10)
print (rcv)
print("121") 
port.write(b"\x1A") # Enable to send SMS
for i in range(1):
    rcv = port.read(10)
    print (rcv)
