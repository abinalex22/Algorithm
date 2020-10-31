# Write your code here :-)
from microbit import *

display.show("M")
def get_data(i):

    counter = 0
    for counter in range(0, 10001):
        if counter == 10000:
            f = running_time()
            b = (f - i) / 1000
    print(b)


def run():
    i = running_time()
    get_data(i)
run()
display.show("B")
