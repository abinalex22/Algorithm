# Write your code here :-)
from microbit import *
t_in_Celsius = temperature()
def converter(t):
    t =9/5*t +32
    return t
display.show(Image.HAPPY)
while True:
    if button_a.was_pressed():
        display.scroll(str(t_in_Celsius))
    elif button_b.was_pressed():
        t_in_Fahrenheit = converter(t_in_Celsius)
        display.scroll(str(t_in_Fahrenheit))

