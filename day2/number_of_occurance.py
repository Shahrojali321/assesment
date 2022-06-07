"""Defination:Program that accept some words and count the number of distinct words"""
def counter(lst):
    """Algorithm to count the number of distint words """
    dictonary={}
    for variable in lst:
        if variable not in dictonary.keys():
            dictonary[variable]=1
        else:
            dictonary[variable]=dictonary[variable]+1
    for j in dictonary.keys():
        print(j,":",dictonary[j])
if __name__=='__main__':
    LIST=[]
    counter(LIST)
    list_length=int(input("enter the length of list: "))
    for i in range(0,list_length):
        element=input("Enter the element of a list: ")
        LIST.append(element)
    print(LIST)
    print(f"the length of list is: {list_length}")
