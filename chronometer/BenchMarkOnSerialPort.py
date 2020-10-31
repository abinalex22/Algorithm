import serial
#the port will depend on your computer
#for a linux it will probably be /dev/ttyACM0
#PORT = "/dev/ttyACM0"
#for windows it will be COM(something), typically COM 6 or COM 11
PORT = "COM6"
import time
BAUD = 115200
s = serial.Serial(PORT)
s.baudrate = BAUD
s.parity   = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE
print("started")

#read a line from the microbit, decode it and strip the whitespace at the end
try:
    data = s.readline().decode("ascii").rstrip()

#split the string into several substrings separated by " "
    data_s = data.split(" ")
    print("BenchMark of Microbit",data_s[0])
# get the following strings and tranform the into int
finally:
    s.close()
i = time.time()
for counter in range(0,10001):
    if counter == 10000:
        f = time.time()
        print("BenchMark of system",(f-i)/1000)
