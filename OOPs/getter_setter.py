class car:
    def __init__(self, a = 40):
        self._speed = a

    def get_speed(self):
        return self._speed
    def set_speed(self, a):
        self._speed = a
        return



car1 = car()
print(car1.get_speed())
car1.set_speed(90)
print(car1.get_speed())
car1.speed = 100
print(car1.speed)