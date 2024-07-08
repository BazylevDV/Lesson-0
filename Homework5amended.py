immutable_var=("a","b","c", 1,2)#неизменяемый кортеж с списком и цифрами
print("Immutable_var: ",immutable_var)
mutable_list=([3,2,9,"6,6,6"])
print(mutable_list)
mutable_list=([(3,2,9)*2,("6,6,6,")+(":Number")])#изменили кортеж путем умножения элементов цифр и сложения элементов списков
print(mutable_list)
print(immutable_var[1])#выводимна экран 2-ой элемент списка в кортеже immutable_var
immutable_var[2]=6
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
