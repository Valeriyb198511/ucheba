a = int(input("Введите результаты пробежки первого дня в километрах: "))
b = int(input("Введите общий желаемый результат в километрах: "))
days = 1
km = a
while km < b:
    a = a + 0.1 * a
    days += 1
    km = km + a
print(f"Вы достигнете требуемых показателей на %.d день" % days)

