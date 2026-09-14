import random

class Car:
    def __init__(self, reg, max_speed, speed, distance):
        self.reg = reg
        self.max_speed = max_speed
        self.speed = speed
        self.distance = distance

    def accelerate(self, change):
        self.speed += change

        if self.speed < 0:
            self.speed = 0

        if self.speed > self.max_speed:
            self.speed = self.max_speed

    def drive(self, hours):
        self.distance += hours * self.speed


cars = []

for i in range(1, 11):
    random_speed = random.randint(100, 200)
    cars.append(Car(f"ABC-{i}", random_speed, 0, 0))


race_over = False

while not race_over:
    for car in cars:
        random_acceleration = random.randint(-10, 15)

        car.accelerate(random_acceleration)
        car.drive(1)

        if car.distance >= 10000:
            race_over = True
            break


print(f"{'Registration':<15}{'Max speed':<15}{'Speed':<15}{'Distance':<15}")
print("-" * 55)


for car in cars:
    print(f"{car.reg:<15} {car.max_speed:<15} {car.speed:<15} {car.distance:<15}")