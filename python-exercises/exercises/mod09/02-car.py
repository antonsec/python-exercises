class Car:
    def __init__(self,reg, max_speed, speed, distance):
        self.reg = reg
        self.max_speed = max_speed
        self.speed = speed
        self.distance = distance
    def accelerate(self, change):
        self.speed += change
        if self.speed > 142:
            self.speed = 142
        elif self.speed < 0:
            self.speed = 0


car = Car('ABC-123', 142, 0, 0)

car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
print (f"Registeration: {car.reg}\nMax speed: {car.max_speed}km/h\nCurrent speed: {car.speed}km/h\nDsitance traveled: {car.distance}km(s)\n")

car.accelerate(-200)
print (f"Registeration: {car.reg}\nMax speed: {car.max_speed}km/h\nCurrent speed: {car.speed}km/h\nDsitance traveled: {car.distance}km(s)")