#! python3
# Пирамидальная сортировка. Временная сложность:
# 1. Худшая O(n * log(n))
# 2. Средняя O(n * log(n))
# 3. Лучшая O(n * log(n))

def heapsort(alist):
    build_max_heap(alist)
    for i in range(len(alist) - 1, 0, -1):
        alist[0], alist[i] = alist[i], alist[0]
        max_heapify(alist, index=0, size=i)


def parent(i):
    return (i - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def build_max_heap(alist):
    length = len(alist)
    start = parent(length - 1)
    while start >= 0:
        max_heapify(alist, index=start, size=length)
        start = start - 1


def max_heapify(alist, index, size):
    l = left(index)
    r = right(index)
    if l < size and alist[l] > alist[index]:
        largest = l
    else:
        largest = index
    if r < size and alist[r] > alist[largest]:
        largest = r
    if largest != index:
        alist[largest], alist[index] = alist[index], alist[largest]
        max_heapify(alist, largest, size)


num_list = input('Enter the list of numbers: ').split()
num_list = [int(x) for x in num_list]
heapsort(num_list)
print('Sorted list: ', end='')
print(num_list)
