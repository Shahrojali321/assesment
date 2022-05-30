"""Defination:Program to Find the Length of a List Using Recursion"""
lst=[]
def length_lst(lst):
    if (lst==[]):
        return 0
    return 1+length_lst(lst[1:])
n=int(input("enter the number of elements in list: "))
for i in range(0,n):
    element=input("Enter the element of a list: ")
    lst.append(element)
print(lst)
result=length_lst(lst)
print(f"The length of list is: {result}")