# Задание 2
# Дорога
class Road():
    def __init__(self, l, w):
        try:
            self._length = int(l)
            self._width = int(w)
        except ValueError:
            print("try input again")
    def m_cover(self, st_sq, st_th):
        try:
            m = self._length * self._width * int(st_sq) * int(st_th)
            return round(m/1000, 1)
        except ValueError:
            print("try input again")

new_road = Road(input("Length: "), input("Width: "))
print("Materail for road-building, t: ",
      new_road.m_cover(input("Standarts, mass/square: "), input("Standarts, thikness: ")))
