#A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
#UP 5
#DOWN 3
#LEFT 3
#RIGHT 2
import  math
def robot():
    dirx, diry = 0, 0
    while True:
        movement = input("Enter the steps or just press enter if no further movement : ")
        if not movement:
            break
        direction, steps = movement.split(" ")
        if direction == 'RIGHT':
            dirx += int(steps)
        elif direction == 'LEFT':
            dirx -= int(steps)
        elif direction == 'UP':
            diry += int(steps)
        elif direction == 'DOWN':
            diry -= int(steps)
    print(dirx, diry)
    print("Final Distance is {0}".format(round(math.sqrt((dirx**2) + (diry**2)))))

robot()

