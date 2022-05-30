"""Defination:Program that accept some words and count the number of distinct words"""
lst=[]
def counter(lst):
    dict={}
    for i in lst:
        if i not in dict.keys():
            dict[i]=1
        else:
            dict[i]=dict[i]+1
    
    for j in dict.keys():
        print(j,":",dict[j])
counter(lst)
n=int(input("enter the length of list: "))
for i in range(0,n):
    element=input("Enter the element of a list: ")
    lst.append(element)
print(lst)
print(f"the length of list is: {n}")