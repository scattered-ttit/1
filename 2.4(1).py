import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    surname TEXT,
    patronymic TEXT,
    group_name TEXT,
    grade1 INTEGER,
    grade2 INTEGER,
    grade3 INTEGER,
    grade4 INTEGER
)
''')
conn.commit()

# === ФУНКЦИИ ===
def add_student():
    name = input("Имя: ")
    surname = input("Фамилия: ")
    patronymic = input("Отчество: ")
    group = input("Группа: ")
    grades = [int(input(f"Оценка {i+1}: ")) for i in range(4)]
    cursor.execute('INSERT INTO students (name, surname, patronymic, group_name, grade1, grade2, grade3, grade4) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                   (name, surname, patronymic, group, *grades))
    conn.commit()
    print("✅ Студент добавлен.")

def view_all_students():
    cursor.execute("SELECT id, name, surname, group_name FROM students")
    for row in cursor.fetchall():
        print(row)

def view_student():
    student_id = int(input("ID студента: "))
    cursor.execute("SELECT * FROM students WHERE id=?", (student_id,))
    row = cursor.fetchone()
    if row:
        avg = sum(row[5:9]) / 4
        print(f"Студент: {row[1]} {row[2]} {row[3]}, Группа: {row[4]}, Оценки: {row[5:9]}, Средний балл: {avg:.2f}")
    else:
        print("❌ Студент не найден.")

def edit_student():
    student_id = int(input("ID студента для редактирования: "))
    name = input("Новое имя: ")
    surname = input("Новая фамилия: ")
    patronymic = input("Новое отчество: ")
    group = input("Новая группа: ")
    grades = [int(input(f"Новая оценка {i+1}: ")) for i in range(4)]
    cursor.execute('''
    UPDATE students SET name=?, surname=?, patronymic=?, group_name=?, grade1=?, grade2=?, grade3=?, grade4=?
    WHERE id=?
    ''', (name, surname, patronymic, group, *grades, student_id))
    conn.commit()
    print("✏️ Студент обновлён.")

def delete_student():
    student_id = int(input("ID студента для удаления: "))
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    print("🗑️ Студент удалён.")

def average_by_group():
    group = input("Введите название группы: ")
    cursor.execute("SELECT grade1, grade2, grade3, grade4 FROM students WHERE group_name=?", (group,))
    rows = cursor.fetchall()
    if rows:
        total = sum(sum(row) for row in rows)
        count = len(rows) * 4
        print(f"📊 Средний балл по группе {group}: {total / count:.2f}")
    else:
        print("❌ Группа не найдена.")

# === МЕНЮ ===
def menu():
    while True:
        print("\n--- МЕНЮ ---")
        print("1. Добавить студента")
        print("2. Просмотреть всех студентов")
        print("3. Просмотреть одного студента")
        print("4. Редактировать студента")
        print("5. Удалить студента")
        print("6. Средний балл по группе")
        print("0. Выход")

        choice = input("Выберите пункт: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_all_students()
        elif choice == "3":
            view_student()
        elif choice == "4":
            edit_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            average_by_group()
        elif choice == "0":
            break
        else:
            print("❗ Неверный выбор.")

menu()
conn.close()
