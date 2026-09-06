class Car:
    def __init__(self,reg, max_speed, curr_speed, distance):
        self.reg = reg
        self.max_speed = max_speed
        self.curr_speed = curr_speed
        self.distance = distance

car = Car('ABC-123', 142, 0, 0)

print (f"Registeration: {car.reg}\nMax speed: {car.max_speed}km/h\nCurrent speed: {car.curr_speed}km/h\nDsitance traveled: {car.distance}km(s)")