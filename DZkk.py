from pprint import pprint

def read_cookbook():
    cook_book = {}
    with open('C:/Users/Юрий/Desktop/PytonDZ/Открытие и чтение файлов/hello.txt', 'r', encoding='utf-8') as f:
        for line in f:
            dish_name = line.strip()
            #print(dish_name)
            count = int(f.readline())
            ing_list = list()
            for item in range(count):
                ingrs = {}
                ingr = f.readline().strip()
                ingrs['ingredient_name'], ingrs['quantity'], ingrs['measure'] = ingr.split('|')
                ingrs['quantity'] = int(ingrs['quantity'])
                ing_list.append(ingrs)
            f.readline()
            cook_book[dish_name] = ing_list
        return cook_book
#Нужно написать функцию, которая на вход принимает список блюд из cook_book и количество персон для кого мы будем готовить
def get_shop_list_by_dishes(dishes, person_count):
    ingr_list = dict()

    for dish_name in dishes:  # итерируем список полученных блюд
        if dish_name in cook_book:
            for ings in cook_book[dish_name]:  # итерируем ингридиенты в блюде
                meas_quan_list = dict()
                if ings['ingredient_name'] not in ingr_list:
                    meas_quan_list['measure'] = ings['measure']
                    meas_quan_list['quantity'] = ings['quantity'] * person_count
                    ingr_list[ings['ingredient_name']] = meas_quan_list
                else:
                    ingr_list[ings['ingredient_name']]['quantity'] = ingr_list[ings['ingredient_name']]['quantity'] + \
                                                                     ings['quantity'] * person_count

        else:
            print(f'\n"Такого блюда нет в списке!"\n')
    return ingr_list
'''
Пример Даны файлы: 1.txt

Строка номер 1 файла номер 1
Строка номер 2 файла номер 1
2.txt

Строка номер 1 файла номер 2
Итоговый файл:

2.txt
1
Строка номер 1 файла номер 2
1.txt
2
Строка номер 1 файла номер 1
Строка номер 2 файла номер 1
'''
def rewrite_file(path1=None, path2=None, path3=None):
    if path1 or path2 or path3 is None:
        path1 = 'C:/Users/Юрий/Desktop/PytonDZ/Открытие и чтение файлов/1.txt'
        path2 = 'C:/Users/Юрий/Desktop/PytonDZ/Открытие и чтение файлов/2.txt'
        path3 = 'C:/Users/Юрий/Desktop/PytonDZ/Открытие и чтение файлов/3.txt'
        outout_file = "C:/Users/Юрий/Desktop/PytonDZ/Открытие и чтение файлов/rewrite_file.txt"
        
        with open(path1, 'r', encoding='utf-8') as f1:
            file1 = f1.readlines()
        with open(path2, 'r', encoding='utf-8') as f2:
            file2 = f2.readlines()
        with open(path3, 'r', encoding='utf-8') as f3:
            file3 = f3.readlines()
        with open(outout_file, 'w', encoding='utf-8') as f_total:

            if len(file1) < len(file2) and len(file1) < len(file3):
                f_total.write(path1 + '\n')
                f_total.write(str(len(file1)) + '\n')
                f_total.writelines(file1)
                f_total.write('\n')
            elif len(file2) < len(file1) and len(file2) < len(file3):
                f_total.write(path2 + '\n')
                f_total.write(str(len(file2)) + '\n')
                f_total.writelines(file2)
                f_total.write('\n')
            elif len(file3) < len(file1) and len(file3) < len(file2):
                f_total.write(path3 + '\n')
                f_total.write(str(len(file3)) + '\n')
                f_total.writelines(file3)
                f_total.write('\n')
            if len(file2) > len(file1) > len(file3) or len(file2) < len(file1) < len(
                    file3):
                f_total.write(path1 + '\n')
                f_total.write(str(len(file1)) + '\n')
                f_total.writelines(file1)
                f_total.write('\n')
            elif len(file1) > len(file2) > len(file3) or len(file2) > len(file1) and len(file2) < len(
                    file3):
                f_total.write(path2 + '\n')
                f_total.write(str(len(file2)) + '\n')
                f_total.writelines(file2)
                f_total.write('\n')
            elif len(file1) > len(file3) > len(file2) or len(file3) > len(file1) and len(file3) < len(
                    file2):
                f_total.write(path3 + '\n')
                f_total.write(str(len(file3)) + '\n')
                f_total.writelines(file3)
                f_total.write('\n')
            if len(file1) > len(file2) and len(file1) > len(file3):
                f_total.write(path1 + '\n')
                f_total.write(str(len(file1)) + '\n')
                f_total.writelines(file1)
            elif len(file2) > len(file1) and len(file2) > len(file3):
                f_total.write(path2 + '\n')
                f_total.write(str(len(file2)) + '\n')
                f_total.writelines(file2)
            elif len(file3) > len(file1) and len(file3) > len(file2):
                f_total.write(path3 + '\n')
                f_total.write(str(len(file3)) + '\n')
                f_total.writelines(file3)
    else:
        print('Не надо параметры')
    return


cook_book = read_cookbook()
print('Задание 1')
print(cook_book)
print('Задание 2')
pprint(get_shop_list_by_dishes(dishes=['Запеченный картофель', 'Омлет', 'Щи'], person_count=2))
rewrite_file()
