def calculate_sum_of_numbers_and_length_of_strings(data):
    total_sum_numbers = 0
    total_string_length = 0

    if isinstance(data, (list, tuple, set)):
        for item in data:
            total = calculate_sum_of_numbers_and_length_of_strings(item)
            if isinstance(total, tuple):
                sum_numbers, string_length = total
                total_sum_numbers += sum_numbers
                total_string_length += string_length
            else:
                total_sum_numbers += total
    elif isinstance(data, dict):
        for key, value in data.items():
            total = calculate_sum_of_numbers_and_length_of_strings(key)
            if isinstance(total, tuple):
                sum_numbers, string_length = total
                total_sum_numbers += sum_numbers
                total_string_length += string_length
            else:
                total_sum_numbers += total

            total = calculate_sum_of_numbers_and_length_of_strings(value)
            if isinstance(total, tuple):
                sum_numbers, string_length = total
                total_sum_numbers += sum_numbers
                total_string_length += string_length
            else:
                total_sum_numbers += total
    elif isinstance(data, str):
        total_string_length += len(data)
    elif isinstance(data, (int, float)):
        total_sum_numbers += data

    return total_sum_numbers + total_string_length


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_sum_of_numbers_and_length_of_strings(data_structure)
print(f"Сумма чисел и длин строк: {result}")
