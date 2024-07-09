immutable_var=("a,b,c", (1,2))#неизменяемый кортеж с списком и цифрами
print("Immutable_var: ",immutable_var)
mutable_list=[3,2,9,"6,6,6"]#создаем список из 2-х элементов
print(mutable_list)
mutable_list=[(3,2,9)*2,("6,6,6,")+(":Number")]#изменили  путем умножения элементов цифр и сложения элементов списков
print(mutable_list)
mutable_list[0]="Inclusive world"#заменяем первый элемент в списке
print(mutable_list)
print(immutable_var[1])#выводим на экран 2-ой элемент  в кортеже immutable_var
immutable_var[0]="Акция: цена при покупке 2 шт"# хочу поменять первый элемент в кортеже
print(immutable_var)# кортеж не изменяем по элементам




# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
