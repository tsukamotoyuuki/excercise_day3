from ex6_1 import Car


class Truck(Car):
    def __init__(self, seats, max_speed, capacity):
        super().__init__(seats, max_speed)
        self.__capacity = capacity

    @property
    def capacity(self):
        return self.__capacity

    def spec(self):
        print(f"Seats: {self.seats}, Max_speed: {self.max_speed}, Capacity: {self.__capacity}")


if __name__ == '__main__':
    Truck = Truck(7, 90, 500)
    Truck.spec()
