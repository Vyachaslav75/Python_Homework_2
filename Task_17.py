import random


def write_file(user_list):
    with open('file.txt', 'w', encoding='utf-8') as f:
        if len(user_list):
            for i in user_list:
                f.writelines(str(i)+'\n')
        f.close()


def read_file():
    with open('file.txt', 'r', encoding='utf-8') as f:
        result = []
        for i in f:
            result.append(int(i))
        f.close()
    return result


def index_list(count_index):
    print('Если хотите ввести индексы нажмите 1')
    print('Для заполнения случайными индексами нажмите 2')
    user_str = input('Введите номер режима заполнения файла:  ')
    if user_str == '1':
        user_str = input(
            f'Введите номера индексов через запятую, максимум {count_index}:  ')
        user_str = [int(x) for x in user_str.split(',')]
    elif user_str == '2':
        user_str = []
        for i in range(count_index//2):
            user_str.append(random.randint(0, count_index-1))
    write_file(user_str)


while True:
    try:
        user_number = int(input('Введите число:  '))
        break
    except ValueError:
        print('Введите целое цисло')
user_list = []
for i in range(-user_number, user_number+1):
    user_list.append(i)
# print(f'Список для рассчета  {user_list}')
# write_file(user_list)
index_list(len(user_list))
print(f'Список для рассчета  {user_list}')
index = read_file()
print(f'Номера индексов для умножения  {index}')
res = 1
for i in index:
    res *= user_list[i]
print(f'Произведение элементов: {res}')
