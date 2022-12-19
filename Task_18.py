import random
while True:
    try:
        user_number = int(input('Введите длину списка:  '))
        break
    except ValueError:
        print('Введите целое цисло')
user_list = []
for i in range(user_number):
    user_list.append(random.randint(-user_number, user_number))
print(f'Сгенерированный список:       {user_list}')
user_list1 = user_list[:]
random.shuffle(user_list)
print(f'Перемешанный shuffle список:  {user_list}')
for i in range(len(user_list1)-1, 0, -1):
    rand_ind = random.randint(0, i)
    user_list1[i], user_list1[rand_ind] = user_list1[rand_ind], user_list1[i]
print(f'Перемешанный список:          {user_list1}')
