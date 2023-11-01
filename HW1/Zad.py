# Дан список целых чисел numbers

numbers = [3, 6, 1, 4, 8, 2, 9]


# Задача 1
# Необходимо написать в императивном стиле процедуру
# для сортировки числа в списке в порядке убывания.
# Можно использовать любой алгоритм сортировки.

def sort_list_imperative(numbers):
    numbers_copy = numbers.copy()  # чтобы не менять значение списка за пределами функции
    sorted_numbers = []

    while numbers_copy:
        num_min = max(numbers_copy)
        sorted_numbers.append(num_min)
        numbers_copy.remove(num_min)

    return sorted_numbers


sorted_numbers = sort_list_imperative(numbers)
print("Отсортированный список:", sorted_numbers)


# Задача 2
# Написать точно такую же процедуру, но в декларативном стиле

def sort_list_declarative(numbers):
    return sorted(numbers, reverse=True)


sorted_numbers = sort_list_declarative(numbers)
print("Отсортированный список:", sorted_numbers)
