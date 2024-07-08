my_dict={'Арина':2005,'Денис':2013,'Юля':1985}# cоздали словарь по дням рождения
print(my_dict)
print(my_dict.get('Арина'))
print(my_dict.get('Антон'))
my_dict.update({'Лариса':1966,'Дмитрий':1969})# добавили новые пары ключей и значений
print(my_dict)#вывели обновленный словарь
my_dict.pop(('Арина'))#удаляем одну из пар по ключу "Арина"
print(my_dict)
my_set={"пробирки c крышками и без, диаметром в мм ",9,12,16,9,12,8,9,12,7,18}#создан ассортимент пробирок
print(my_set)# выведем уникальные диаметры
my_set.update({"Т хранинеия летом от-до",(8,25),float(10.5)})#  добавим новые элементы для покупателей
print(my_set)# выведем на печать
print(my_set.discard(7))#выводим неликвидный диаметр пробирок из прайса
print(my_set)#публикуем отредактированный ассортимент





# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
