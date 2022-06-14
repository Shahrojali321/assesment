"""Defination:Program to Count Total Number of Words in a String"""
def reverse_list(list1):
    """Algorithm to reverse list element"""
    reverse_list1=[]
    for items in range(list_length-1,-1,-1):
        element=list1[items]
        reverse_list1.append(element)
    return reverse_list1
if __name__=='__main__':
    LIST1=[]
    list_length=int(input("Enter the length of list: "))
    for i in range(list_length):
        ELEMENT=int(input("Enter the elements of list: "))
        LIST1.append(ELEMENT)
    print(reverse_list(LIST1))
