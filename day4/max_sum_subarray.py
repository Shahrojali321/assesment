"Defination:Program to Solve Maximum Subarray Problem using Divide and Conquer"
import sys
 
"""Function to find the maximum sublist sum using divide-and-conquer"""
def maximum_sum(my_array, left=None, right=None):
 
    if not my_array:
        return 0
    if left is None and right is None:
        left, right = 0, len(my_array) - 1
    if right == left:
        return my_array[left]

    mid = (left + right) // 2

    left_max = -sys.maxsize
    total = 0
    for i in range(mid, left - 1, -1):
        total += my_array[i]
        if total > left_max:
            left_max = total
 
    right_max = -sys.maxsize
    total = 0        
 
    for i in range(mid + 1, right + 1):
        total += my_array[i]
        if total > right_max:
            right_max = total
 
    """Recursively find the maximum sublist sum"""
    maxLeftRight = max(maximum_sum(my_array, left, mid),
                    maximum_sum(my_array, mid + 1, right))
    return max(maxLeftRight, left_max + right_max)

my_array=[] 
array_length =int(input("Enter the length of array: "))
for element in range(0,array_length):
    element=int(input("Enter the elements of array: "))
    my_array.append(element)
print(my_array)

print(f"The Maximum sum of the subarray is : {maximum_sum(my_array)}")