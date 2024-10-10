def print_params(a=1, b=True, c="string"):
    print(a, b, c)


print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print_params(a=6, b=False, c="integer")

values_list = [1, False, "two"]
values_dict = {"a": 7, "b": False, "c": "What"}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [1.4, 4]

print_params(*values_list_2, 42)
# работает только pycharm, подсвечивает 42 как переменную a
