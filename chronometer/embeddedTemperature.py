from microbit import *

REFRESH = 1000

def get_data():
    x = temperature()
    print("Temperature:",x)

def run():
 while True:
  sleep(REFRESH)
  get_data()

display.show('T')
run()
