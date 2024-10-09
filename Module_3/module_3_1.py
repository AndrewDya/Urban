calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(str_arg):
    count_calls()
    str_len = len(str_arg)
    str_upp = str_arg.upper()
    str_low = str_arg.lower()
    return str_len, str_upp, str_low


def is_contains(str_arg, list_arg):
    count_calls()
    str_arg_up = str_arg.upper()
    return str_arg_up in (item.upper() for item in list_arg)


# Примеры вызовов функций
result1 = string_info("Hello, World!")
print(result1)

result2 = is_contains("UrbaN", ["urban", "city", "town"])
print(result2)

result3 = is_contains("House", ["home", "apartment", "building"])
print(result3)

result4 = string_info("Python programming")
print(result4)

print("Количество вызовов функций:", calls)