"""Defination:Program to Find the Largest and Smallest Item in a Tuple"""
lst=[]
def largest_smallest(Tuple):
    tup_largest = Tuple[0]
    tup_smallest=Tuple[0]
    for i in Tuple:
        if(tup_largest < i):
            tup_largest = i
        if(tup_smallest > i):
            tup_smallest = i
    print(f"The lasgest number in tuple is: {tup_largest}")
    print(f"The smallest number in touple is : {tup_smallest}")
n=int(input("enter the length of tuple: "))
for i in range(0,n):
    element=input("Enter the element of a tuple: ")
    lst.append(element)
Tuple=tuple(lst)
print(Tuple)
result=largest_smallest(Tuple)
