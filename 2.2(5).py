class MyClass:
    def __init__(self, a=0, b=0):  # Конструктор с параметрами и по умолчанию
        self.a = a
        self.b = b
        print(f"Создан объект: a = {self.a}, b = {self.b}")

    def show(self):
        print(f"Значения: a = {self.a}, b = {self.b}")

    def __del__(self):  # Деструктор
        print(f"Объект с a = {self.a}, b = {self.b} удалён")

print("Создание объекта по умолчанию:")
obj1 = MyClass()  # по умолчанию a=0, b=0
obj1.show()
print("\nСоздание объекта с параметрами:")
obj2 = MyClass(10, 20)
obj2.show()
print("\nКонец программы. Объекты будут удалены автоматически.")
