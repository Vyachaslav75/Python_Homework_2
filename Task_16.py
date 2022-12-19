while True:
    user_number = input('Введите целое число: ')
    try:
        user_number = int(user_number)
        break
    except ValueError:
        print('Введите число')
sum=0
user_dict={}
for i in range(1, user_number+1):
    user_dict[i]=round((1+1/i)**i, 2)
    sum+=user_dict[i]
print(f'n={user_number}  {user_dict}')
print(f'Сумма  {sum:3.2f}')