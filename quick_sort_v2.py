import time

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)


num_list = input('Enter the list of numbers: ').split()

start = time.time()

num_list = [int(x) for x in num_list]
sorted_list = quicksort(num_list)

elapsed = time.time() - start

print('Sorted list: ', end='')
print(sorted_list)
print('Time:', elapsed)
