a = float(input("Введите выручку фирмы: "))
b = float(input("Введите издержки фирмы: "))
if a > b:
    print(f"Фирма получает прибыль. Рентабельность выручки составила {a / b:.2f}")
    c = int(input("Введите количество сотрудников фирмы: "))
    print(f"Прибыль в расчете на одного сотрудника составила {a / c:.2f}")
elif a == b:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")
