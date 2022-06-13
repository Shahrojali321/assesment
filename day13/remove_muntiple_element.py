"""Defination:Program to Remove multiple elements from a list """
def remove_element(list1,unwanted):
    """Algorithm to remove elements"""
    for element in unwanted:
        for j in list1:
            if j==element:
                list1.remove(element)
    return list1
if __name__=='__main__':
    LIST1=[]
    UNWANTED=[]
    list_length=int(input("Enter the length of list: "))
    for char in range(0,list_length):
        elements=int(input("Enter the element of list: "))
        LIST1.append(elements)
    print(f"original list : \n {LIST1}")
    unwanted_length=int(input("Enter the length of list containing unwanted elements: "))
    for char in range(0,unwanted_length):
        elements=int(input("Enter the element to remove: "))
        UNWANTED.append(elements)
    print(f"unwanted elements: \n {UNWANTED}")
    print(f"The final list is : \n {remove_element(LIST1,UNWANTED)}")
