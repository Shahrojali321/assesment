"Defination:Program to Solve Maximum Subarray Problem using Divide and Conquer"
import sys
def maximum_sum(my_array, left=None, right=None):
    """Function to find the maximum sublist sum using divide-and-conquer"""
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
    max_left_right = max(maximum_sum(my_array, left, mid),
                    maximum_sum(my_array, mid + 1, right))
    return max(max_left_right, left_max + right_max)
if __name__=='__main__':
    MY_ARRAY=[]
    array_length =int(input("Enter the length of array: "))
    for element in range(0,array_length):
        element=int(input("Enter the elements of array: "))
        MY_ARRAY.append(element)
    print(MY_ARRAY)
    print(f"The Maximum sum of the subarray is : {maximum_sum(MY_ARRAY)}")
