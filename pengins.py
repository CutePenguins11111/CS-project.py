from djitellopy import tello
from time import sleep

tim = tello.Tello()
tim.connect()
print(tim.get_battery())


