from djitellopy import tello
from time import sleep

tim = tello.Tello()
tim.connect()
print(tim.get_battery())

# taking off and moving

tim.takeoff()
tim.move_up(120)
tim.move_forward(400)
tim.move_forward(400)

# turning

tim.rotate_counter_clockwise(90)
tim.move_forward(400)
tim.rotate_counter_clockwise(90)

# Final half

tim.move_forward(400)
tim.move_forward(400)
tim.rotate_counter_clockwise(90)
tim.move_forward(400)
tim.move_down(120)
tim.land()
