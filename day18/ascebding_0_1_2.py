"""Defination:Sort the array in ascending order"""
def sort_arr(arr):
    """Algorithm to sort """
    list_0=[]
    list_1=[]
    list_2=[]
    final_list=[]
    for char in arr:
        if char==0:
            list_0.append(char)
        elif char==1:
            list_1.append(char)
        else:
            list_2.append(char)
    final_list=list_0+list_1+list_2
    return final_list
if __name__=='__main__':
    ARRAY=[]
    list_length=int(input("Enter the length of list: "))
    for element in range(list_length):
        elements=int(input("Enter the element of list: "))
        ARRAY.append(elements)
    print(f"The original array is : \n {ARRAY}")
    print(f"The sorted array is : {sort_arr(ARRAY)}")
