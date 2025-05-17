import psutil
import sqlite3
from datetime import datetime

# Создание базы и таблицы
conn = sqlite3.connect('system_monitor.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS system_stats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    cpu_load REAL,
    memory_used REAL,
    memory_total REAL,
    disk_used REAL,
    disk_total REAL
)
''')
conn.commit()

# === ФУНКЦИИ ===

# 1. Сбор и сохранение данных
def collect_data():
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    cursor.execute('''
        INSERT INTO system_stats (timestamp, cpu_load, memory_used, memory_total, disk_used, disk_total)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (timestamp, cpu, mem.used / (1024 ** 3), mem.total / (1024 ** 3),
          disk.used / (1024 ** 3), disk.total / (1024 ** 3)))

    conn.commit()
    print("✅ Данные сохранены:", timestamp)

# 2. Просмотр последних записей
def view_data():
    cursor.execute("SELECT * FROM system_stats ORDER BY id DESC LIMIT 10")
    rows = cursor.fetchall()
    for row in rows:
        print(f"\n🕒 {row[1]}")
        print(f"🧠 CPU загрузка: {row[2]}%")
        print(f"📊 Память: {row[3]:.2f}ГБ / {row[4]:.2f}ГБ")
        print(f"💾 Диск: {row[5]:.2f}ГБ / {row[6]:.2f}ГБ")

# === МЕНЮ ===
def menu():
    while True:
        print("\n=== СИСТЕМНЫЙ МОНИТОР ===")
        print("1. Провести мониторинг")
        print("2. Посмотреть последние записи")
        print("0. Выход")
        choice = input("Выберите пункт: ")

        if choice == "1":
            collect_data()
        elif choice == "2":
            view_data()
        elif choice == "0":
            break
        else:
            print("❗ Неверный выбор")

menu()
conn.close()
