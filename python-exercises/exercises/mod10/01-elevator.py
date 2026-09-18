class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.floor = bottom_floor

    def floor_up(self):
            self.floor += 1
            print (f"Elevator is now on floor {self.floor}")

    def floor_down(self):

            self.floor -= 1
            print (f"Elevator is now on floor {self.floor}")

    def go_to_floor(self, floor):
            if floor > self.top_floor:
                floor = self.top_floor
            elif floor < self.bottom_floor:
                  floor = self.bottom_floor
            
            while self.floor < floor:
                self.floor_up()

            while self.floor > floor:
                self.floor_down()

    
elevator = Elevator(0, 10)

elevator.go_to_floor(20)
print ("")
elevator.go_to_floor(0)