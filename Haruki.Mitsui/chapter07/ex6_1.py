class Car:
    def __init__(self, seats, max_speed):
        self.__seats = seats
        self.__max_speed = max_speed

    def __eq__(self, other):
        if not isinstance(self, Car):
            return False
        return self.__seats == other.__seats and self.__max_speed == other.__max_speed

    @property
    def seats(self):
        return self.__seats

    @property
    def max_speed(self):
        return self.__max_speed

    def spec(self):
        print(f"Seats: {self.__seats}, Max_speed: {self.__max_speed}")


class Truck(Car):
    def __init__(self, seats, max_speed, capacity):
        super().__init__(seats, max_speed)
        self.__capacity = capacity

    @property
    def capacity(self):
        return self.__capacity

    def spec(self):
        print(f"Seats: {self.seats}, Max_speed: {self.max_speed}, Capacity: {self.__capacity}")


car1 = Car(4, 100)
Truck = Truck(7, 90, 500)
car3 = Car(4, 100)
car1.spec()
Truck.spec()
car3.spec()
print(car1 == car3)
