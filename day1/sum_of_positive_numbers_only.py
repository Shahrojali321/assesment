"""Defination: Summation of positive numbers """
lst=[]
def summ(lst):
    num=0
    for i in range(0,n):
        if(lst[i]>=0):
            num=num+lst[i]
    return num
n=int(input("enter the length of list: "))
for i in range(0,n):
    element=int(input("Enter the element of a list: "))
    lst.append(element)
print(f"The list on mubers is : {lst}")
result=summ(lst)
print(f"The Summation of positive inputs is : {result}")
        