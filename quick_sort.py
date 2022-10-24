#! python3
# Быстрая сортировка. Временная сложность:
# 1. Худшая O(n^2)
# 2. Средняя O(n * log(n))
# 3. Лучшая O(n * log(n))

def quicksort(alist, start, end):
    """Sorts the list from indexes start to end - 1 inclusive."""
    if end - start > 1:
        p = partition(alist, start, end)
        quicksort(alist, start, p)
        quicksort(alist, p + 1, end)


def partition(alist, start, end):
    pivot = alist[start]
    i = start + 1
    j = end - 1

    while True:
        while i <= j and alist[i] <= pivot:
            i = i + 1
        while i <= j and alist[j] >= pivot:
            j = j - 1

        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
        else:
            alist[start], alist[j] = alist[j], alist[start]
            return j


num_list = input('Enter the list of numbers: ').split()
num_list = [int(x) for x in num_list]
quicksort(num_list, 0, len(num_list))
print('Sorted list: ', end='')
print(num_list)
