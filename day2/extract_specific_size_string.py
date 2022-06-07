"""Defination: program to extract specified size of strings from a give list of string values"""
lst=[]
def list_string(size):
    """Algorithm to extract the specific size of string"""
    lst2=[]
    for i in lst:
        if(len(i)==size):
            lst2.append(i)
        else:
            lst2=['no element found']
    return lst2
if __name__=='__main__':
    list_length=int(input("enter the length of list: "))
    for elements in range(0,list_length):
        element=input("Enter the element of a list: ")
        lst.append(element)
    print(lst)
    SIZE=int(input("Enter the size of a string which wants to extract from the list: "))
    result=list_string(SIZE)
    print(f"The required list of string: {result}")
