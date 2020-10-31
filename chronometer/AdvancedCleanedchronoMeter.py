# Add your Python code here. E.g.
#This program will show you the 3 symbols while you run , Play ||, Pause ||, Stop [] your chronometer
from microbit import *


class Chronometer:
    def __init__(self, state):
        self.intermed = [0] # storing all the intermediateStopChrono points in a list
        self.stopPoint = [0] # storing all the stop points in a list, initiate with 0 at first index
        self.state = 0

    def runChrono(self):
        self.a_pressed_time = running_time()
        self.state = 1 #sets state to 1
        sleep(300) # this is the minimum delay that has to be given before launching
        display.show(Image("09090:09090:09090:09090:09090")) # when the chronometer is running it will show the pause button ||

    def stopChrono(self):
        self.newtime = running_time() # get the current time when a is pressed
        self.b_time = self.stopPoint[-1] + self.newtime - self.a_pressed_time #intially self.stopPoint[-1] =0 for first time
        self.stopPoint.append(self.b_time) # store the b_time for the next time when stopped, this value will be added
        self.state = 2  # set the state value to 2
        display.show(self.b_time) # display the time after the a is pressed
        display.show(Image("09000:09900:09990:09900:09000")) #when paused it will show the play button, that can be pressed by ||

    def intermediateStopChrono(self):
        self.state = 1
        self.newtime = running_time() # get the current time
        self.i_time = self.stopPoint[-1] + self.newtime - self.a_pressed_time #get the new time
        self.intermed.append(self.i_time) # store the intermediate time just for future purpose
        display.show(self.i_time)
        display.show(Image("09090:09090:09090:09090:09090")) # when the chronometer is running it will show the pause button ||

    def resetChrono(self):
        display.show(Image("00000:09990:09990:09990:00000")) # when pressed shows the stop sign []
        #set all the value to 0
        self.state = 0
        self.intermed = [0]
        self.stopPoint = [0]
        self.a_pressed_time = 0
        self.b_time = 0
        self.i_time = 0

    def launchChrono(self): #launches with
        while True:
            if self.state == 0:
                if button_a.is_pressed():
                    self.runChrono()
                elif button_b.is_pressed():
                    self.resetChrono()
            elif self.state == 1:
                if button_a.is_pressed():
                    self.stopChrono()
                elif button_b.is_pressed():
                    self.intermediateStopChrono()
            elif self.state == 2:
                if button_a.is_pressed():
                    self.runChrono()
                elif button_b.is_pressed():
                    self.resetChrono()


chron = Chronometer(0)
display.show(Image.ARROW_W)
chron.launchChrono()


"""

intial state:   i
button:         b
final state:    f
Logic table
|i|-->|b|-->|f|
------------
|0|-->|a|-->|1|
|0|-->|b|-->|0|
|1|-->|a|-->|2|
|1|-->|b|-->|1|
|2|-->|a|-->|1|
|2|-->|b|-->|0|
"""
