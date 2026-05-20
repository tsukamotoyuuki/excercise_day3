from excercise_day3.wangyan.chapter07.ex07_1 import Car

class Truck(Car):
    def __init__(self,seats,max_speed,capacity):
        super().__init__(seats,max_speed)
        self.capacity = capacity

    def spec(self):
        print("Seats:", self.seats)
        print("Max speed:", self.max_speed)
        print("Capacity:",self.capacity)

T = Truck(4,100,500)
T.spec()