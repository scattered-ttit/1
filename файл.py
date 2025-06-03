def input_list_elements():
    elements = []
    while True:
        s = input("Введите элемент (пустая строка - выход): ")
        if s == "":
            break
        elements.append(s)

    if elements:
        shortest = min(elements, key=len)
        longest = max(elements, key=len)
        print("Самый короткий элемент:", shortest)
        print("Самый длинный элемент:", longest)
    else:
        print("Список пуст.")