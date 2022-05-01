# Задание 3
# Работник
class Worker():
    def __init__(self, name, surname, position, w, b):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": w, "bonus": b}
class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname
    def get_total_income(self):
        inc  = self._income.values()
        return sum(inc)

new_worker1 = Position("Rick", "Berch", "manager", 10000, 3000)
new_worker2 = Position("Mark", "Tailor", "manager", 30000, 0)
print(f"{new_worker1.get_full_name():<20}: {new_worker1.get_total_income()} USD")
print(f"{new_worker2.get_full_name():<20}: {new_worker2.get_total_income()} USD")