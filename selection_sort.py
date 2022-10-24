#! python3
# Сортировка выбором. Временная сложность:
# 1. Худшая O(n^2)
# 2. Средняя O(n^2)
# 3. Лучшая O(n^2)

def selection_sort(alist):
    for i in range(0, len(alist) - 1):
        smallest = i
        for j in range(i + 1, len(alist)):
            if alist[j] < alist[smallest]:
                smallest = j
        alist[i], alist[smallest] = alist[smallest], alist[i]


num_list = input('Enter the list of numbers: ').split()
num_list = [int(x) for x in num_list]
selection_sort(num_list)
print('Sorted list: ', end='')
print(num_list)
