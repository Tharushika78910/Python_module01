import random
import math

points = int(input("How many points do you want to generate : "))
points_inside = 0
i=0
while i < points:
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if x**2 + y**2 < 1:
        points_inside += 1
    i += 1
pi = 4 * points_inside / points
print(f"The estimation for Pi is {pi}")
print(f"The difference with math Pi is : {math.pi - pi}")
