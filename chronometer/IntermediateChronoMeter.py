# Write your code here :-)
from microbit import *


class IntermediateChronometer:
    def __init__(self, state):
        self.state = 0

    def runChrono(self):
        self.a_pressed_time = running_time()
        self.state = 1
        sleep(300)
        display.show(Image("09090:09090:09090:09090:09090"))

    def stopChrono(self):
        self.newtime = running_time()
        self.b_time = self.newtime - self.a_pressed_time
        self.state = 2
        display.show(self.b_time)
        display.show(Image("09000:09900:09990:09900:09000"))

    def intermediateStopChrono(self):
        self.state = 1
        self.newtime = running_time()
        self.i_time = self.newtime - self.a_pressed_time
        display.show(self.i_time)
        display.show(Image("09090:09090:09090:09090:09090"))

    def resetChrono(self):
        display.show(Image("00000:09990:09990:09990:00000"))
        self.state = 0


chron = IntermediateChronometer(0)
display.show(Image.ARROW_W)
while True:
    if chron.state == 0:
        if button_a.is_pressed():
            chron.runChrono()
        elif button_b.is_pressed():
            chron.resetChrono()
    elif chron.state == 1:
        if button_a.is_pressed():
            chron.stopChrono()
        elif button_b.is_pressed():
            chron.intermediateStopChrono()
    elif chron.state == 2:
        if button_b.is_pressed():
            chron.resetChrono()
