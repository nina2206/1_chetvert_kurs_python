# Задание 4
# Машины
from random import randint
class Car():
    def __init__(self, na, co, sp):
        self.speed = sp
        self.color = co
        self.name = na
    def go(self):
        return " is riding"
    def stop(self):
        return " was stoped"
    def direction(self):
        return "'s changed direction"
    def show_speed(self):
        return self.speed
class TownCar(Car):
    def __init__(self, na, co, sp):
        super().__init__(na, co, sp)
        self.is_police = False
    def show_speed(self):
        if self.speed > 60:
           return "Speed is more then 60 km/h. Slow down!"
class SportCar(Car):
    def __init__(self, na, co, sp):
        super().__init__(na, co, sp)
        self.is_police = False
class WorkCar(Car):
    def __init__(self, na, co, sp):
        super().__init__(na, co, sp)
        self.is_police = False
    def show_speed(self):
        if self.speed > 40:
           return "Speed is more then 40 km/h. Slow down!"
class PoliceCar(Car):
    def __init__(self, na, co, sp):
        super().__init__(na, co, sp)
        self.is_police = True
    def show_speed(self):
            if self.speed > 60:
                return "Police car is following a crimer"

drive = ""
car1 = TownCar("Lada", "red", randint(1, 120))
car2 = WorkCar("DAF", "silver", randint(1, 120))
car3 = SportCar("Ferrari", "red", randint(40, 180))
car4 = PoliceCar("Ford", "white", randint(1, 180))
while drive != "q":
    drive = input("Choose any car:  1 - TownCar, 3 - WorkCar, 7 - SportCar,9 - PoliceCar, - or 'q' to exit")
    if drive == "1":
        print(car1.name, end="")
        print(car1.go())
        print(f"speed is {car1.speed}")
        print(car1.name, end="")
        print(car1.direction())
        print(car1.name, end="")
        print(car1.stop())
        print("Speed control:", car1.show_speed())
    elif drive == "3":
        print(car2.name, end="")
        print(car2.go())
        print(f"speed is {car2.speed}")
        print(car2.name, end="")
        print(car2.direction())
        print(car2.name, end="")
        print(car2.stop())
        print("Speed control:", car2.show_speed())
    elif drive == "7":
        print(car3.name, end="")
        print(car3.go())
        print(f"speed is {car3.speed}")
        print(car3.name, end="")
        print(car3.direction())
        print(car3.name, end="")
        print(car3.stop())
        print("Speed control:", car3.show_speed())
    elif drive == "9":
        police_car = (f"{car4.name} is a police car" if car4.is_police == True else "")
        print(police_car)
        print(f"{car4.name}", end="")
        print(car4.go())
        print(f"speed is {car3.speed}")
        print(car4.name, end="")
        print(car4.direction())
        print(car4.name, end="")
        print(car4.stop())
        print("Speed control:", car4.show_speed())
    else:
        break
