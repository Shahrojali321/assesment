"""Defination:Program for Binary Insertion Sort"""
def binary_insertion_sort(my_list):
    """algorithm for binary sort"""
    for i in range(1, len(my_list)):
        temp = my_list[i]
        position = binary_search(my_list, temp, 0, i) + 1
        for k in range(i, position, -1):
            my_list[k] = my_list[k - 1]
        my_list[position] = temp
def binary_search(my_list, num, start, end):
    """algorihm for binary search"""
    if end - start <= 1:
        if num < my_list[start]:
            return start - 1
        else:
            return start
    mid = (start + end)//2
    if my_list[mid] < num:
        return binary_search(my_list, num, mid, end)
    elif my_list[mid] > num:
        return binary_search(my_list, num, start, mid)
    else:
        return mid
if __name__=='__main__':
    MY_LIST = input('Enter the list of numbers: ').split()
    MY_LIST = [int(x) for x in MY_LIST]
    binary_insertion_sort(MY_LIST)
    print(f'Sorted list: {MY_LIST}')
