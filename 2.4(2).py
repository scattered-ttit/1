import sqlite3

conn = sqlite3.connect("ilovedrink.db")
cursor = conn.cursor()

# Таблицы
cursor.execute('''
CREATE TABLE IF NOT EXISTS drinks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    strength REAL,
    stock INTEGER
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS cocktails (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    strength REAL,
    price REAL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS cocktail_ingredients (
    cocktail_id INTEGER,
    drink_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY(cocktail_id) REFERENCES cocktails(id),
    FOREIGN KEY(drink_id) REFERENCES drinks(id)
)
''')
conn.commit()

# === ФУНКЦИИ ===

# 1. Добавление напитка
def add_drink():
    name = input("Название напитка: ")
    strength = float(input("Крепость (%): "))
    stock = int(input("Остаток (мл): "))
    cursor.execute("INSERT INTO drinks (name, strength, stock) VALUES (?, ?, ?)", (name, strength, stock))
    conn.commit()
    print("✅ Напиток добавлен")

# 2. Просмотр напитков
def view_drinks():
    cursor.execute("SELECT * FROM drinks")
    for row in cursor.fetchall():
        print(row)

# 3. Добавление коктейля
def add_cocktail():
    name = input("Название коктейля: ")
    price = float(input("Цена (₽): "))
    ingredients = []
    total_strength = 0
    total_volume = 0

    print("Добавьте ингредиенты коктейля (введите 0 для завершения):")
    while True:
        view_drinks()
        drink_id = int(input("ID напитка (0 - завершить): "))
        if drink_id == 0:
            break
        quantity = int(input("Количество (мл): "))
        cursor.execute("SELECT strength FROM drinks WHERE id=?", (drink_id,))
        strength = cursor.fetchone()[0]
        total_strength += strength * quantity
        total_volume += quantity
        ingredients.append((drink_id, quantity))

    if total_volume == 0:
        print("❌ Невозможно создать коктейль без ингредиентов.")
        return

    strength = total_strength / total_volume
    cursor.execute("INSERT INTO cocktails (name, strength, price) VALUES (?, ?, ?)", (name, strength, price))
    cocktail_id = cursor.lastrowid

    for drink_id, quantity in ingredients:
        cursor.execute("INSERT INTO cocktail_ingredients (cocktail_id, drink_id, quantity) VALUES (?, ?, ?)",
                       (cocktail_id, drink_id, quantity))

    conn.commit()
    print("🍹 Коктейль добавлен.")

# 4. Просмотр коктейлей
def view_cocktails():
    cursor.execute("SELECT * FROM cocktails")
    for row in cursor.fetchall():
        print(f"{row[0]}: {row[1]} | Крепость: {row[2]:.1f}% | Цена: {row[3]}₽")

# 5. Продажа напитка
def sell_drink():
    view_drinks()
    drink_id = int(input("ID напитка для продажи: "))
    quantity = int(input("Сколько мл продать: "))
    cursor.execute("SELECT stock FROM drinks WHERE id=?", (drink_id,))
    stock = cursor.fetchone()[0]
    if stock < quantity:
        print("❌ Недостаточно на складе.")
    else:
        cursor.execute("UPDATE drinks SET stock = stock - ? WHERE id=?", (quantity, drink_id))
        conn.commit()
        print("✅ Продажа выполнена.")

# 6. Продажа коктейля
def sell_cocktail():
    view_cocktails()
    cocktail_id = int(input("ID коктейля: "))
    cursor.execute("SELECT * FROM cocktail_ingredients WHERE cocktail_id=?", (cocktail_id,))
    ingredients = cursor.fetchall()

    for ing in ingredients:
        drink_id, qty = ing[1], ing[2]
        cursor.execute("SELECT stock FROM drinks WHERE id=?", (drink_id,))
        stock = cursor.fetchone()[0]
        if stock < qty:
            print(f"❌ Недостаточно ингредиента ID {drink_id}. Продажа отменена.")
            return

    for ing in ingredients:
        drink_id, qty = ing[1], ing[2]
        cursor.execute("UPDATE drinks SET stock = stock - ? WHERE id=?", (qty, drink_id))
    conn.commit()
    print("✅ Коктейль продан.")

# 7. Пополнение запасов
def restock():
    view_drinks()
    drink_id = int(input("ID напитка: "))
    amount = int(input("Сколько мл добавить: "))
    cursor.execute("UPDATE drinks SET stock = stock + ? WHERE id=?", (amount, drink_id))
    conn.commit()
    print("📦 Запас обновлён.")

# === МЕНЮ ===
def menu():
    while True:
        print("\n=== I Love Drink ===")
        print("1. Добавить напиток")
        print("2. Просмотр напитков")
        print("3. Добавить коктейль")
        print("4. Просмотр коктейлей")
        print("5. Продать напиток")
        print("6. Продать коктейль")
        print("7. Пополнить запасы")
        print("0. Выход")

        choice = input("Выберите пункт: ")
        if choice == "1": add_drink()
        elif choice == "2": view_drinks()
        elif choice == "3": add_cocktail()
        elif choice == "4": view_cocktails()
        elif choice == "5": sell_drink()
        elif choice == "6": sell_cocktail()
        elif choice == "7": restock()
        elif choice == "0":
            break
        else:
            print("❗ Неверный выбор")

menu()
conn.close()
