class Train:
    def __init__(self, dest, num, time):
        self.dest = dest
        self.num = num
        self.time = time
    def show(self):
        print(f"Поезд №{self.num} до {self.dest} отправляется в {self.time}")
trains = [
    Train("Москва", 101, "12:30"),
    Train("Питер", 202, "15:45"),
    Train("Томск", 70, "19:50")

]
num = int(input("Введите номер поезда: "))
for t in trains:
    if t.num == num:
        t.show()

