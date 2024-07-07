my_string=input("Укажите оборудование для ремонта:  ")# программа-смета по подсчету стоимости ремонта оборудования
print("Ремонту подлежит(ат) :",my_string)
cost_of_repair=int(input("Цена ремонта 1 оборудования, ($): "))
number_items=int(input("Необходимо отремонтировать, (шт): "))
total_budget=int(number_items*cost_of_repair)
print("Смета ремонта :",total_budget,"($).") #стоимость затрат на ремонт всего оборудования
my_strings=input("Укажите название сервисной организации:  ".upper())# меняем на верхний регистр строку
my_strings=input("Укажите фамилию и инициалы инженера: ".lower())# меняем на нижний регистр строку
date=input("Человеко часов: ".replace (' ','' ))# убираем пробелы в строке согласно ДЗ
name=input("A,B,C: -класс опасности работ :  ")
print(name,"-указан тип работ, подпись_____ (ФИО)")
name=input("Оценка работ от 1 до 5:   ")
print("Утверждено:", name,"____ФИО " )
name="Минздрав"
print(name[0],name[-1])#первый и последний элемент строки в переменной name согласно ДЗ




# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
