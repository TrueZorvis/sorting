#! python3
# Сортировка пузырьком. Временная сложность:
# 1. Худшая O(n^2)
# 2. Средняя O(n^2)
# 3. Лучшая O(n)

def bubble_sort(nums):
    for i in range(len(nums) - 1, 0, -1):
        no_swap = True
        for j in range(0, i):
            if nums[j+1] < nums[j]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                no_swap = False
        if no_swap:
            return


num_list = input('Enter the list of numbers: ').split()
num_list = [int(x) for x in num_list]
bubble_sort(num_list)
print('Sorted list: ', end='')
print(num_list)
