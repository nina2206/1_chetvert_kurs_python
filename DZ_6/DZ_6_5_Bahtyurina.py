# Задание 5
# канцтовары
class Stationery():
    def __init__(self, t):
        self.title = t
    def draw(self):
        return "Start drawing"
class Pen(Stationery):
    def draw(self):
        if self.title == 1:
            return "Drawing with a pen"
class Pencil(Stationery):
    def draw(self):
        if self.title == 2:
            return "Drawing with a pencil"
class Handle(Stationery):
    def draw(self):
        if self.title == 3:
            return "Drawing with a handle"
my_item = ""
while my_item != "q":
    my_item = input("Choose your item: 1 - pen, 2 - pencil, 3 - handle")
    print(Stationery(my_item).draw())
    if my_item == "1":
        my_item = Pen(1)
        print(my_item.draw())
    elif my_item == "2":
        my_item = Pencil(2)
        print(my_item.draw())
    elif my_item == "3":
        my_item = Handle(3)
        print(my_item.draw())
    else:
        break

