"""Defination:Program to find list items greater than average"""
def greater_than_average(list1):
    """Algorithm for items greater than average"""
    list2=[]
    summation=0
    average=0
    for variable in list1:
        summation=summation+variable
    average=summation/len(list1)
    print(average)
    for char in list1:
        if char>average:
            list2.append(char)
    return list2
if __name__=='__main__':
    LIST1=[]
    list_length=int(input("Enter the length of list: "))
    for elements in range(list_length):
        element=int(input("Enter the elements of list: "))
        LIST1.append(element)
    print(f"{greater_than_average(LIST1)}")
