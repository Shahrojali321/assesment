"""Defination: program to extract specified size of strings from a give list of string values"""
lst=[]
lst2=[]
def list_string(size):
    for i in lst:
        if(len(i)==size):
            lst2.append(i)
        else:
            lst2=['no element found']
    return lst2
n=int(input("enter the length of list: "))
for i in range(0,n):
    element=input("Enter the element of a list: ")
    lst.append(element)
print(lst)
size=int(input("Enter the size of a string which wants to extract from the list: "))
result=list_string(size)
print(f"The required list of string: {result}")