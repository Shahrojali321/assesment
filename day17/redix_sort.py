"""Defination:Program for implementation of Radix Sort"""
from functools import reduce
def radix(list1):
    """Algorithm for radix sort"""
    num_digits = __get_num_digits(list1)
    for digit in range(0, num_digits):
        list2 = [[] for i in range(10)]
        for item in list1:
            num = item // 10 ** (digit) % 10
            list2[num].append(item)
        list1 = __flatten(list2)
        return list1
# flatten into a 1D List
def __flatten(list1):
    return reduce(lambda x, y: x + y, list1)
# get number of digits in largest item
def __get_num_digits(list1):
    maximum = 0
    for item in list1:
        maximum = max(maximum, item)
    return len(str(maximum))
if __name__=='__main__':
    MY_LIST = [55, 45, 3, 289, 213, 1, 288, 53, 2]
    print(radix(MY_LIST))
    