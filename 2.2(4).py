class Counter:
    def __init__(self, value=0):  # значение по умолчанию или заданное пользователем
        self.value = value
        print(f"Счётчик создан со значением: {self.value}")

    def increase(self):  # увеличение на 1
        self.value += 1

    def decrease(self):  # уменьшение на 1
        self.value -= 1

    def get_value(self):  # текущее значение
        return self.value
print("Создание счётчика по умолчанию:")
c1 = Counter()
c1.increase()
c1.increase()
c1.decrease()
print("Текущее значение c1:", c1.get_value())
print("\nСоздание счётчика с начальным значением 10:")
c2 = Counter(10)
c2.decrease()
c2.decrease()
print("Текущее значение c2:", c2.get_value())
