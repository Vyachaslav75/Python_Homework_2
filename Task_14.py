while True:
    user_number = input('Введите вещественное число: ')
    try:
        check = float(user_number)
        break
    except ValueError:
        print('Введите число')
user_number = [int(x) for x in user_number if x.isdigit()]
sum = 0
for i in user_number:
    sum += i
print(f'{check} -> {sum}')
