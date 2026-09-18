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
    
class Building:
      def __init__(self, bottom_floor, top_floor, number_of_elevators):
            self.bottom_floor = bottom_floor
            self.top_floor = top_floor
            self.number_of_elevators = number_of_elevators
            self.elevators = []

            for i in range(number_of_elevators):
                  self.elevators.append(Elevator(bottom_floor, top_floor))
      
      def run_elevator(self, elevator_number, destination_floor):
                print (f"Elevator {elevator_number}:")
                self.elevators[elevator_number - 1].go_to_floor(destination_floor)

      def fire_alarm(self):
                for i in range(self.number_of_elevators):
                    self.elevators[i].go_to_floor(building.bottom_floor)

building = Building(0, 10, 3)

building.run_elevator(3, 7)
print ("")
building.fire_alarm()
