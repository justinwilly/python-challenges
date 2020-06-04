"""
From code challenge lecture by Kapil Sharma on 4 Jun 2020.
​
"Return the square of the sorted ints" is the initial instruction.
Given: an array of sorted ints: they can be neg, 0, and/or pos.
Assume ints are distinct.
​
The catch here is that ints can be negative, so their squares might be bigger than a pos int's square.
"""
# This version has time complexity of O(n) + O(n log n), simplified to O(n log n).
# And space complexity of O(1) since numbers are replaced in place.

def sorted_squared_arr1(nums):
    if nums == None or len(nums) == 0:
        return nums
​
    for i, num in enumerate(nums):
        nums[i] = num**2
​
    nums.sort()
    return nums
​
# The version below improves the time complexity to O(n). Each num is only visited once.
# It takes advantage of the fact that the input arr is sorted.
# However, increases space complexity to O(n).

def sorted_squared_arr2(nums):
    # First, deal with edge cases
    if nums == None or len(nums) == 0:
        return nums
​
    # Now, initiate vars
    output_arr = []
    # 2 pointers that we will move to the intersection of neg and non-neg numbers.
    left_index = 0
    right_index = 0
    length = len(nums)
​
    # Find the last neg num in arr
    while right_index < length and nums[right_index] < 0:
        right_index += 1
​
    # Now right_index should be at the first non-negative num.
    # Move left_index to be right_index - 1, so it's at the last neg num.
    left_index = right_index - 1
​
    while left_index >= 0 and right_index < length:
        # Compare the 2 squared values to see which one is smaller.
        # Add that one to the output_arr and adjust the corresponding pointer.
        if nums[left_index] ** 2 < nums[right_index] ** 2:
            output_arr.append(nums[left_index]**2)
            left_index -= 1
        else:
            output_arr.append(nums[right_index]**2)
            right_index += 1
​
    # Now, deal with the leftovers (since previous loop will end when just one of the conditions are true)
​
    while left_index >= 0:
        output_arr.append(nums[left_index] ** 2)
        left_index -= 1
​
    while right_index < length:
        output_arr.append(nums[right_index] ** 2)
        right_index += 1
​
    return output_arr
​
# This last version uses an output array that is initialized at a specified size,
# and uses a pointer for the output_array_index. The instructor did it this way (but in C).
# This could be more space efficient.
​
​
def sorted_squared_arr3(nums):
    # First, deal with edge cases
    if nums == None or len(nums) == 0:
        return nums
    # Now, initiate vars'
    length = len(nums)
    output_arr = [0] * length
    # 2 pointers that we will move to the intersection of neg and non-neg numbers.
    left_index = 0
    right_index = 0
    output_arr_pointer = 0
​
    # Find the last neg num in arr
    while right_index < length and nums[right_index] < 0:
        right_index += 1
​
    # Now right_index should be at the first non-negative num.
    # Move left_index to be right_index - 1, so it's at the last neg num.
    left_index = right_index - 1
​
    while left_index >= 0 and right_index < length:
        # Compare the 2 squared values to see which one is smaller.
        # Add that one to the output_arr and adjust the corresponding pointer.
        if nums[left_index] ** 2 < nums[right_index] ** 2:
            output_arr[output_arr_pointer] = nums[left_index]**2
            left_index -= 1
​
        else:
            output_arr[output_arr_pointer] = nums[right_index]**2
            right_index += 1
​
        output_arr_pointer += 1
​
    # Now, deal with the leftovers (since previous loop will end when just one of the conditions are true)
​
    while left_index >= 0:
        output_arr[output_arr_pointer] = nums[left_index]**2
        left_index -= 1
        output_arr_pointer += 1
​
    while right_index < length:
        output_arr[output_arr_pointer] = nums[right_index]**2
        right_index += 1
        output_arr_pointer += 1
​
    return output_arr
​
​
print(sorted_squared_arr1([-10, -6, -5, 0, 2, 3, 7]))
print(sorted_squared_arr2([-10, -6, -5, 0, 2, 3, 7]))
print(sorted_squared_arr3([-10, -6, -5, 0, 2, 3, 7]))