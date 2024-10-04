# Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Используя этот список составьте второй список primes содержащий только простые числа.
# А так же третий список not_primes, содержащий все не простые числа.
# Выведите списки primes и not_primes на экран(в консоль).
# Пункты задачи:
#
#     Создайте пустые списки primes и not_primes.
#     При помощи цикла for переберите список numbers.
#     Напишите ещё один цикл for (вложенный), где будут подбираться делители для числа из 1ого цикла.
#     Отметить простоту числа можно переменной is_prime, записав в неё занчение True перед проверкой.
#     В процессе проверки на простоту записывайте числа из списка numbers в списки primes и not_primes в зависимости от значения переменной is_prime после проверки (True - в prime, False - в not_prime).
#     Выведите списки primes и not_primes на экран(в консоль).

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = False

for num in numbers:
    if num == 1:
        continue
    for j in range(1, numbers[num - 1]):
        if num % j == 0 and num != j and j != 1:
            is_prime = False
            break
        else:
            is_prime = True
    if is_prime:
        primes.append(num)
    else:
        not_primes.append(num)

print(f"Простые {primes}")
print(f"Сложные {not_primes}")
