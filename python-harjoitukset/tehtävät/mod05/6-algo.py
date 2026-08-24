import random

points = int(input("Total amount of random points: "))

countdown = points

inside_points = 0
while countdown >= 1:
    countdown -= 1
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        inside_points += 1
    
pi = 4 * inside_points / points
print (pi)