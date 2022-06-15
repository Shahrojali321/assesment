"""Defination:Program to print even length words in a string"""
def odd_string(list1):
    """algorithm to get even string list"""
    list2=[]
    for char in list1:
        if len(char)%2==0:
            list2.append(char)
    return list2
if __name__=='__main__':
    LIST1=[]
    list_length=int(input("enter the length of list: "))
    for element in range(0,list_length):
        elements=input("Enter the element of string")
        LIST1.append(elements)
    print(f"The original list is : \n {LIST1}")
    print(f"The even string list is; \n {odd_string(LIST1)}")
