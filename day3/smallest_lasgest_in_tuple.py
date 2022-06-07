"""Defination:Program to Find the Largest and Smallest Item in a Tuple"""
def largest_smallest(tuple1):
    """Algorithm for largest and smallest in tuple"""
    tup_largest = tuple1[0]
    tup_smallest=tuple1[0]
    for char in tuple1:
        if(tup_largest < char):
            tup_largest = char
        if(tup_smallest > char):
            tup_smallest = char
    print(f"The lasgest number in tuple is: {tup_largest}")
    print(f"The smallest number in touple is : {tup_smallest}")
if __name__=='__main__':
    lst=[]
    list_length=int(input("enter the length of tuple: "))
    for i in range(0,list_length):
        element=input("Enter the element of a tuple: ")
        lst.append(element)
    TUPLE=tuple(lst)
    print(TUPLE)
    largest_smallest(TUPLE)
