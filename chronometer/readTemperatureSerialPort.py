import serial
#the port will depend on your computer
#for a linux it will probably be /dev/ttyACM0
#PORT = "/dev/ttyACM0"
#for windows it will be COM(something), typically COM 6 or COM 11
PORT = "COM6"

BAUD = 115200
count =0
s = serial.Serial(PORT)
s.baudrate = BAUD
s.parity   = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE

try:
    while True:
        count += 1
        #read a line from the microbit, decode it and strip the whitespace at the end
        data = s.readline().decode("ascii").rstrip()
        
        #split the string into several substrings separated by " "
        data_s = data.split(" ")
        #print(data_s)
        
        # get the first string
        message = data_s[0]
        
        
        # get the following strings and tranform the into int
        x = int(data_s[1])
        print(message,x)
    
finally:
    s.close()
    
