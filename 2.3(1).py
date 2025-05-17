class Worker:
    def __init__(self, name, surname, rate, days):
        self.name = name
        self.surname = surname
        self.rate = rate
        self.days = days

    def GetSalary(self):
        return self.rate * self.days

# Демонстрация:
worker1 = Worker("Иван", "Иванов", 1000, 20)
print(f"{worker1.name} {worker1.surname} заработал: {worker1.GetSalary()} руб.")

worker2 = Worker("Мария", "Петрова", 1200, 18)
print(f"{worker2.name} {worker2.surname} заработала: {worker2.GetSalary()} руб.")
