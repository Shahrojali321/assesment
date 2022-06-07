"""defination:Program to Create a Class and Get All Possible Subsets"""
def subsets_lst(lst,lst2=None,variable=0):
    """For subsets"""
    if lst2==None:
        lst2=[0] * len(lst)
    if variable>=len(lst):
        subset=[str(lst[i]) for i in range(len(lst)) if lst2[i]==1]
        print("{"+",".join(subset) + "}")
    else:
        lst2[variable]=0
        subsets_lst(lst,lst2,variable+1)
        lst2[variable]=1
        subsets_lst(lst,lst2,variable+1)
if __name__=='__main__':
    LIST=[]
    #To create a list
    n=int(input("enter the number of elements in list: "))
    for i in range(0,n):
        element=input("Enter the element of a list: ")
        LIST.append(element)
    print(LIST)
    subsets_lst(LIST)
