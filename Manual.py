"""
Manual mode for the robot.
Allows the robot to be controlled manually using the keyboard.
W = forward, S = backward, A = left, D = right.
"""
import pi2go
import readchar
#Speed of the robot 0-100 (Percentage of maximum speed/duty cycles per motor). The default is 50.
speed = 50

#
pi2go.init()


try:
    while True:
        key = readchar.readkey()


        if key == "w" or key == "W":
            pi2go.forward(speed)
        elif key == "s" or key == "S":
            pi2go.backward(speed)
        elif key == "a" or key == "A":
            pi2go.left(speed)
        elif key == "d" or key == "D":
            pi2go.right(speed)
        elif key == "q" or key == "Q":
            pi2go.stop()
            break


finally:
    pi2go.stop()
    pi2go.cleanup()
