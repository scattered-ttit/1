class Student:
    def __init__(self, surname, birth, group, grades):
        self.surname = surname
        self.birth = birth
        self.group = group
        self.grades = grades
    def change_info(self, surname=None, birth=None, group=None):
        if surname: self.surname = surname
        if birth: self.birth = birth
        if group: self.group = group
    def show(self):
        print(f"{self.surname}, {self.birth}, группа: {self.group}, оценки: {self.grades}")
students = [
    Student("Иванов", "2000-01-01", "101", [5, 4, 5, 3, 4]),
    Student("Петров", "1999-02-02", "102", [3, 4, 4, 4, 5])
]
surname = input("Введите фамилию: ")
birth = input("Введите дату рождения: ")
for s in students:
    if s.surname == surname and s.birth == birth:
        s.show()
