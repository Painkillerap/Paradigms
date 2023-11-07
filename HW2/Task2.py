# Определение процедуры merge, которая объединяет два отсортированных массива в один отсортированный.

def merge(left_half, right_half):
    result = []  # Создание пустого списка для объединения левой и правой половин.
    i = j = 0  # Инициализация индексов для объединения двух половин.

    # Объединение левой и правой половин в один отсортированный список.
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:  # Сравнение элементов левой и правой половин.
            result.append(left_half[i])  # Если элемент из левой меньше, добавляем его в результат.
            i += 1
        else:
            result.append(right_half[j])  # Если элемент из правой меньше, добавляем его в результат.
            j += 1

    # Добавление оставшихся элементов из левой и правой половин (если такие есть).
    while i < len(left_half):
        result.append(left_half[i])
        i += 1

    while j < len(right_half):
        result.append(right_half[j])
        j += 1

    return result


# Определение процедуры merge_sort, которая выполняет сортировку методом слияния.

def merge_sort(arr):
    if len(arr) <= 1:  # Проверка, что длина массива меньше или равна 1 (иначе сортировка не нужна).
        return arr
    else:
        mid = len(arr) // 2  # Вычисление середины массива.
        left_half = arr[:mid]  # Создание левой половины массива.
        right_half = arr[mid:]  # Создание правой половины массива.

        # Рекурсивный вызов merge_sort для левой и правой половин массива.
        left_half_sorted = merge_sort(left_half)
        right_half_sorted = merge_sort(right_half)

        # Объединение левой и правой половин в один отсортированный массив.
        return merge(left_half_sorted, right_half_sorted)


my_array = [64, 34, 25, 12, 22, 11, 90]  # Создание неотсортированного массива.
sorted_array = merge_sort(my_array)  # Вызов процедуры сортировки слиянием.
print("Отсортированный массив (Merge Sort):", sorted_array)  # Вывод отсортированного массива.