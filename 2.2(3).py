class Numbers:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def show(self):
        print(f"a = {self.a}, b = {self.b}")
    def change(self, a, b):
        self.a = a
        self.b = b
    def summa(self):
        return self.a + self.b
    def max_value(self):
        return max(self.a, self.b)
n = Numbers(3, 5)
n.show()
print("Сумма:", n.summa())
print("Максимум:", n.max_value())
n.change(10, 2)
n.show()
