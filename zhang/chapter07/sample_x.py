class Car:
    def __init__(self, seats, max_speed):
        self.__seats = seats
        self.__max_speed = max_speed

    @property
    def seats(self):
        return self.__seats

    @property
    def max_speed(self):
        return self.__max_speed

    @seats.setter
    def seats_set(self, seats):
        self.__seats = seats

    @max_speed.setter
    def max_speed_set(self, max_speed):
        self.__max_speed = max_speed

    def spec(self):
        self.seats_set = 4
        self.max_speed_set = 100


class Truck(Car):
    def __init__(self, capacity, seats, max_speed):
        super().__init__(seats, max_speed)
        self.capacity = capacity

    def spec(self):
        self.seats_set = 4
        self.max_speed_set = 100
        self.capacity = 500

car1 = Car(0, 0)
truck1 = Truck(2,2,1)


print(truck1.seats)
print(truck1.max_speed)

# car.seats_set()
# car.max_speed_set()

