import math
radius_circle = int(input("Enter a radius of a circle: "))
length_square = int(input("Enter the side length of a square: "))

result1 = math.pi * radius_circle ** 2

result2 = length_square ** 2

print (f"Circle area: {result1:>.2f} and square area: {result2}")
