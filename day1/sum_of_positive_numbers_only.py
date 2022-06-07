"""Defination:Summation of positive numbers """
def summ(lst):
    """Algorithm to find the sammation """
    num=0
    for i in range(0,list_length):
        if(lst[i]>=0):
            num=num+lst[i]
    return num
if __name__=='__main__':
    LIST=[]
    list_length=int(input("enter the length of list: "))
    for variable in range(0,list_length):
        element=int(input("Enter the element of a list: "))
        LIST.append(element)
    print(f"The list on mubers is : {LIST}")
    result=summ(LIST)
    print(f"The Summation of positive inputs is : {result}")
        