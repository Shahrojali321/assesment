"""Defiantion:Program to Calculate the Average of List Items"""
def average_list(my_list):
    """Algorithm to get average of list"""
    summation=0
    for element in my_list:
        summation=summation+element
    average=summation/len(my_list)
    return average
if __name__=='__main__':
    MY_LIST=[]
    LIST_LENGTH=int(input("Enter the length of list: "))
    for char in range(LIST_LENGTH):
        elements=int(input("Enter the Element of list: "))
        MY_LIST.append(elements)
    print(f"The original list is : \n {MY_LIST}")
    print(f"The average of list is: {average_list(MY_LIST)}")
