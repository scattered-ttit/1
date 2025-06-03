def point_in_circle(x, y, R):
    distance_squared = x**2 + y**2
    if distance_squared <= R**2:
        return True
    else:
        return False

x = float(input("Введите координату x: "))
y = float(input("Введите координату y: "))
R = float(input("Введите радиус круга: "))
if point_in_circle(x, y, R):
    print("Точка принадлежит кругу.")
else:
    print("Точка не принадлежит кругу.")
