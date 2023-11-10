# Функция mean вычисляет среднее значение элементов в массиве
def mean(arr):
    return sum(arr) / len(arr)


# Функция std вычисляет стандартное отклонение массива
def std(arr):
    m = mean(arr)
    return (sum((x - m) ** 2 for x in arr) / len(arr)) ** 0.5


# Функция pearson_correlation вычисляет коэффициент корреляции Пирсона между двумя массивами
def pearson_correlation(x, y):
    mean_x = mean(x)
    mean_y = mean(y)
    std_x = std(x)
    std_y = std(y)

    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(len(x)))
    denominator = len(x) * std_x * std_y

    correlation = numerator / denominator
    return correlation


# Пример использования
x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]
print(pearson_correlation(x, y))
