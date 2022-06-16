"""Defination:Program to Remove Even Numbers in a List"""
def remove_even(my_list):
    """Algorithm to remove even number"""
    list1=[]
    for element in my_list:
        if element%2==1:
            list1.append(element)
    return list1
if __name__=='__main__':
    MY_LIST=[]
    list_length=int(input("Enter the length of list: "))
    for num in range(list_length):
        number=int(input("Enter the number: "))
        MY_LIST.append(number)
    print(f"The Updated list is : \n {remove_even(MY_LIST)}")
