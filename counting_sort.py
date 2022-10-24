#! python3
# Сортировка подсчетом. Временная сложность:
# 1. Худшая O(n + k)
# 2. Средняя O(n + k)
# 3. Лучшая O(n)

def counting_sort(alist, largest):
    c = [0] * (largest + 1)
    for i in range(len(alist)):
        c[alist[i]] = c[alist[i]] + 1

    # Find the last index for each element
    c[0] = c[0] - 1  # to decrement each element for zero-based indexing
    for i in range(1, largest + 1):
        c[i] = c[i] + c[i - 1]

    result = [None] * len(alist)

    # Though it is not required here,
    # it becomes necessary to reverse the list
    # when this function needs to be a stable sort
    for x in reversed(alist):
        result[c[x]] = x
        c[x] = c[x] - 1

    return result


num_list = input('Enter the list of (nonnegative) numbers: ').split()
num_list = [int(x) for x in num_list]
k = max(num_list)
sorted_list = counting_sort(num_list, k)
print('Sorted list: ', end='')
print(sorted_list)
