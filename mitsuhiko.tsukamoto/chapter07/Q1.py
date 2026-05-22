class Car:
    def __init__(self, seats, max_speed):
        self.__seats = seats
        self.__max_speed = max_speed

    @property
    def seats(self):
        return self.__seats

    @property
    def speed(self):
        return self.__speed

    def spec(self):
        print("Seats:" + str(self.__seats) + "," + "Max speed:" + str(self.__max_speed))


class Truck(Car):
    def __init__(self, seats, max_speed, capacity):
        super().__init__(seats, max_speed)
        # self.__seats = seats
        # self.__max_speed = max_speed
        self.__capacity = capacity

    def spec(self):
        print("Seats:" + str(self.seats) + "," + "Max speed:" + str(self.max_speed) + "," + "Max speed:" + str(self.capacity))


# if __name__ == main:
    carA = Car(4, 100)
    carA.spec()

    carB = Car(10, 80)
    carB.spec()

    trA = Truck(4, 100, 500)
    trA.spec()

