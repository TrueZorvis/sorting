#! python3
# Сортировка вставками. Временная сложность:
# 1. Худшая O(n^2)
# 2. Средняя O(n^2)
# 3. Лучшая O(n)

def insertion_sort(alist):
    for i in range(1, len(alist)):
        temp = alist[i]
        j = i - 1
        while j >= 0 and temp < alist[j]:
            alist[j + 1] = alist[j]
            j = j - 1
        alist[j + 1] = temp


num_list = input('Enter the list of numbers: ').split()
num_list = [int(x) for x in num_list]
insertion_sort(num_list)
print('Sorted list: ', end='')
print(num_list)
