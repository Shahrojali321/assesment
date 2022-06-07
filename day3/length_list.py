"""Defination:Program to Find the Length of a List Using Recursion"""
def length_lst(lst):
    """algorithm to find the length of list"""
    if (lst==[]):
        return 0
    return 1+length_lst(lst[1:])
if __name__=='__main__':
    LIST=[]
    n=int(input("enter the number of elements in list: "))
    for i in range(0,n):
        element=input("Enter the element of a list: ")
        LIST.append(element)
    print(LIST)
    result=length_lst(LIST)
    print(f"The length of list is: {result}")
