s = int(input("Введите сумму S: "))
p = int(input("Введите произведение P: "))

x = 1
while x <= 1000:
    if s - x <= 1000 and x * (s - x) == p:
        y = s - x
        print("Задуманные числа:", x, "и", y)
        break
    x += 1
else:
    print("Нет решения для заданных .")