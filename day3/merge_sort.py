def mergeSort(my_list):
    if len(my_list)>1:
        mid = len(my_list)//2
        left_half = my_list[:mid]
        right_half = my_list[mid:]

        mergeSort(left_half)
        mergeSort(right_half)
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
my_list=[]
my_list_length = int(input("Enter the length of list: "))
for element in range(0,my_list_length):
    element=int(input("Enter the Elements of the list1: "))
    my_list.append(element)
print(my_list)

mergeSort(my_list)
print(f"The sorted lis is: {my_list}")