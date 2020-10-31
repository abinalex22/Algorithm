from microbit import *

REFRESH = 500

def get_data():
    x, y, z = accelerometer.get_x(), accelerometer.get_y(), accelerometer.get_z()
    print("acceleration:",x, y, z)

def run():
 while True:
  sleep(REFRESH)
  get_data()

display.show('M')
run()
