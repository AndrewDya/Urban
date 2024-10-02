# Задание "Средний балл":
# Вам необходимо решить задачу из реальной жизни:
# "школьные учителя устали подсчитывать вручную средний балл каждого ученика,
# поэтому вам предстоит автоматизировать этот процесс":
# На вход даны следующие данные:
#     Список: grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
#     Множество: students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#     Список grades содержит списки оценок для каждого ученика в алфавитном порядке.
# Например: 'Aaron' - [5, 3, 3, 5, 4]
#     Множество students содержит неупорядоченную последовательность имён всех учеников в классе.
# Напишите программу, которая составляет словарь, используя grades и students,
# где ключом будет имя ученика, а значением - его средний балл.

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3],
          [5, 5, 5, 4, 5]]

students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

aver_grade = []
for item in grades:
    num = round((sum(item)/len(item)), 2)
    aver_grade.append(num)

sorted_students = sorted(list(students))
student_aver_grade = dict(zip(sorted_students, aver_grade))
print("Ученик: Средний балл", student_aver_grade)
