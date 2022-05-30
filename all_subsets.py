"""defination: program to Create a Class and Get All Possible Subsets from a Set of Distinct Integers"""
lst=[]
def subsets_lst(lst,lst2=None,i=0):
    """For subsets"""
    if lst2==None:
        lst2=[0] * len(lst)
    if i>=len(lst):
        subset=[str(lst[i]) for i in range(len(lst)) if lst2[i]==1]
        print("{"+",".join(subset) + "}")
    else:
        lst2[i]=0
        subsets_lst(lst,lst2,i+1)
        lst2[i]=1
        subsets_lst(lst,lst2,i+1)
"""To create a list"""
n=int(input("enter the number of elements in list: "))
for i in range(0,n):
    element=input("Enter the element of a list: ")
    lst.append(element)
print(lst)
result=subsets_lst(lst)