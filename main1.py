list_ = [8, 9, -5, -3, 1, -10, 8, -10, -5, 0, 5, -4, 0, 10, -8, 1, 6, -6, 6, -9]
# TODO найти сумму, количество и среднее арифметическое уникальных чисел
unique_list_ = list (set (list_ ))
print(sum(unique_list_))
print(len(unique_list_))
mean = sum(unique_list_) / len(unique_list_)
print(round(mean, 5))
