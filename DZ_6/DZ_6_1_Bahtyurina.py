# Задание 1
# Светофор
import time
import itertools
"вариант 1"
# class TrafficLight():
#     __color = ""
#     def running(self):
#         TrafficLight.__color = "красный"
#         print (f"\033[31m {TrafficLight.__color}", end="")
#         time.sleep(7)
#         print(f"\r\033[F\033[K\033[0m {TrafficLight.__color}")
#         TrafficLight.__color = "желтый"
#         print (f"\033[33m {TrafficLight.__color}", end="")
#         time.sleep(2)
#         print(f"\r\033[F\033[K\033[0m {TrafficLight.__color}")
#         TrafficLight.__color = "зеленый"
#         print (f"\033[32m {TrafficLight.__color}", end="")
#         time.sleep(7)
#         print(f"\r\033[F\033[K\033[0m {TrafficLight.__color}")
#
# t_light = TrafficLight()
# q = ""
# while True:
#     if q == "q":
#         break
#     else:
#         print(f"{t_light.running()}", end="")
#     q = input("\r\033[K press 'q' to turn off").lower()
# print("Trafficlight was turned off")

"вариант 2"
#
# class Trafficlight:
#     __colour = [["red", [7, 31]], ["yellow", [2, 33]], ["green", [7, 32]], ["yellow", [2, 33]]]
#     def running(self):
#         for light in itertools.cycle(self.__colour):
#             print(f"\r\033[{light[1][1]}m\033[1m{light[0]}\033[0m", end="")
#             time.sleep(light[1][0])
#
# traf_light = Trafficlight()
# traf_light.running()

"вариант 3"
class Trafficlight:
    __colour = ["    ", [7, 2, 7], ["\033[41m\033[1m", "\033[43m\033[1m", "\033[42m\033[1m"]]
    def running(self):
        col_list = ["", ""]
        for n in itertools.cycle((0, 1, 2)):
            col_list[1] = self.__colour[2][n]
            print(f"\r({col_list[int(n == 0)]}{self.__colour[0]}\033[0m)"
                  f"\r({col_list[int(n == 1)]}{self.__colour[0]}\033[0m)"
                  f"\r({col_list[int(n == 2)]}{self.__colour[0]}\033[0m)", end='')
            time.sleep(self.__colour[1][n])

traf_light = Trafficlight()
traf_light.running()