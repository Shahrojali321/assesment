"""Defination:Program to Implement Merge Sort"""
def merge_sort(my_list):
    """Algorithm to implement merge sort"""
    if len(my_list)>1:
        mid = len(my_list)//2
        left_half = my_list[:mid]
        right_half = my_list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i=j=k=0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                my_list[k]=left_half[i]
                i=i+1
            else:
                my_list[k]=right_half[j]
                j=j+1
            k=k+1
        while i < len(left_half):
            my_list[k]=left_half[i]
            i=i+1
            k=k+1
        while j < len(right_half):
            my_list[k]=right_half[j]
            j=j+1
            k=k+1
if __name__=='__main__':
    MY_LIST=[]
    my_list_length = int(input("Enter the length of list: "))
    for element in range(0,my_list_length):
        element=int(input("Enter the Elements of the list1: "))
        MY_LIST.append(element)
    print(MY_LIST)
    merge_sort(MY_LIST)
    print(f"The sorted lis is: {MY_LIST}")
