# Напишите 4 переменных которые буду обозначать следующие данные:
#
#     Количество выполненных ДЗ (запишите значение 12)
#     Количество затраченных часов (запишите значение 1.5)
#     Название курса (запишите значение 'Python')
#     Время на одно задание (вычислить используя 1 и 2 переменные)
#
# Выведите на экран(в консоль), используя переменные, следующую строку:
# Курс: Python, всего задач:12, затрачено часов: 1.5, среднее время выполнения 0.125 часа.

complite_homework = 12
spent_hours = 1.5
course = "Python"
time_to_one_task = spent_hours / complite_homework
print("Курс: " + course + ", всего задач: " + str(complite_homework) + ", затрачено часов: " + str(spent_hours) + ", среднее время выполнения: " + str(time_to_one_task) + " часа")


