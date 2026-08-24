#using math moduel to make my life easier
import math

radius = float(input(f"Give me a radius of a circle: "))
radius = math.sqrt(radius/math.pi)

print (f"{radius:.3f}")