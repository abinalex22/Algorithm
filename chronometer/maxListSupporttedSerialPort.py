import serial
#the port will depend on your computer
#for a linux it will probably be /dev/ttyACM0
#PORT = "/dev/ttyACM0"
#for windows it will be COM(something), typically COM 6 or COM 11
PORT = "COM6"

BAUD = 115200

s = serial.Serial(PORT)
s.baudrate = BAUD
s.parity   = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE
newList =[]
try:
    while True:
        #read a line from the microbit, decode it and strip the whitespace at the end
        data = s.readline().decode("ascii").rstrip()
        
        #split the string into several substrings separated by " "
        data_s = data.split(" ")
        #print(data_s)
        
        # get the first string
        message = data_s[0]
        #print(message)
        if message == "Traceback":
            break
        newList.append(message)
    print("Max length of my List is ",newList[len(newList)-1])
finally:
    s.close()
