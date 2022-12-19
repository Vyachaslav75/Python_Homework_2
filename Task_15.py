while True:
    user_number = input('Введите целое число: ')
    try:
        user_number = int(user_number)
        break
    except ValueError:
        print('Введите число')
result=[1]
for i in range(1, user_number):
    result.append(result[i-1]*(i+1))
print(f'N={user_number}, тогда {result}')