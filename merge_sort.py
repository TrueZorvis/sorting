#! python3
# Сортировка слиянием. Временная сложность:
# 1. Худшая O(n * log(n))
# 2. Средняя O(n * log(n))
# 3. Лучшая O(n * log(n))

def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1


num_list = input('Enter the list of numbers: ').split()
num_list = [int(x) for x in num_list]
merge_sort(num_list)
print('Sorted list: ', end='')
print(num_list)
