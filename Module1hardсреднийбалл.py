students_ = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}# дан школьный журнал с именами
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]# даны оценки за месяц
My_list=list(students_)#переводим множество в список для работы с каждым элементом списка
print("Вот список класса :")
print(My_list)
print("Выведем результаты ученика: ",My_list[0])
f=(sum(grades[0])/(len(grades[0])))#считаем среднюю оценку ученика за четверть
print("Оценки:",grades[0],", Средняя оценка за четверть:",f)#считаем среднюю оценку 1 элемента в списке учеников
print("Результаты ученика: ",My_list[1])
k=(sum(grades[1])/(len(grades[1])))
print("Оценки:",grades[1],", Средняя оценка за четверть:",k)# аналогичные подсчеты по следующему ученику
print("Результаты ученика: ",My_list[2])
a=(sum(grades[2])/(len(grades[2])))
print("Оценки:",grades[2],", Средняя оценка за четверть:",a)
print("Результаты ученика: ",My_list[3])
m=(sum(grades[3])/(len(grades[3])))
print("Оценки:",grades[3],", Средняя оценка за четверть:",m)
print("Результаты ученика: ", My_list[4])
d= (sum(grades[4]) / (len(grades[4])))
print("Оценки:", grades[3], ", Средняя оценка за четверть:", d)
All_results={My_list[0]:f,My_list[1]:k,My_list[2]:a,My_list[3]:m,My_list[4]:d}# создаем словарь для класса
print("Общая ведомость класса: ",All_results)


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
