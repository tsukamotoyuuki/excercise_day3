class Car():
    def __init__(self,seats,max_speed):
        self.__seats = seats
        self.__max_speed =max_speed


    def spec(self):
        print("Seats:",self.__seats)
        print("Max speed:",self.__max_speed)

    def __eq__(self, other):
        if not isinstance(other,Car):
            return False
        return self.seats == other.seats and self.max_speed == other.max_speed

    @property
    def seats(self):
        return self.__seats

    @seats.setter
    def seats(self,value):
        self.__seats = value

    @property
    def max_speed(self):
        return self.__max_speed

    @max_speed.setter
    def max_speed(self,value):
        self.__max_speed = value


if __name__ == "__main__":
    car1 = Car(4, 100)
    car1.spec()
    car2 = Car(4,100)
    car2.spec()
    print(car1 == car2)


