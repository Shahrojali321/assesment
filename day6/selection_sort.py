"""Defination:Python program to implement selection sort"""
def sorting(my_list):
    """function for the selection sort"""
    for element in range(0, len(my_list) - 1):
        smallest = element
        for charactor in range(element + 1, len(my_list)):
            if my_list[charactor] < my_list[smallest]:
                smallest = charactor
        my_list[element], my_list[smallest] = my_list[smallest], my_list[element]
    return my_list
if __name__=='__main__':  
    list1=input('Enter the list of numbers : ').split()
    MY_LIST=[int(x) for x in list1]
    print(f'List after sorting is : {sorting(MY_LIST)}')
