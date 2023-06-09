n = int(input('Введите количество элементов в списке : ')) # вводим количество элементов в массиве
a = input("Введите через пробел элементы списка: ").split()
A_num = list(map(int, a ))
if len(A_num) != n or n == 0:
    print('Введенные элементы не соответствуют заявленному количеству!')
else:
    X = int(input('задайте число X : '))

# предполагаем, что ближайшее число - первый элемент массива
min_diff = abs(X - A_num[0])
closest = a[0]

# проходим по всем остальным элементам массива
for i in range(1, n):
    # вычисляем разницу между текущим элементом и X
    diff = abs(X - A_num[i])
    # если разница меньше, чем предыдущая минимальная разница
    if diff < min_diff:
        # запоминаем текущий элемент как ближайший
        closest = a[i]
        min_diff = diff

print(closest) # выводим ближайший элемент