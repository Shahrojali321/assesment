"""Defination:Program for Binary Search"""
def search(lst,num):
    """Algorithm for binary search"""
    lower=0
    upper=len(lst)-1
    while lower<=upper:
        mid=(lower+upper)//2
        if lst[mid]==num:
            globals()['pos']=mid
            return True
        else:
            if lst[mid] < num:
                lower=mid
            else:
                upper=mid
if __name__=='__main__':
    POS=-1
    LST=[]
    LIST_LENGTH=int(input("enter the size of the list:"))
    for i in range(0,LIST_LENGTH):
        e=int(input("enter the element of the list:"))
        LST.append(e)
    print(LST)
    NUM=int(input("Enter the number to search: "))
    if search(LST,NUM):
        print("The number found in the list at position of: ",POS+1)
    else:
        print("Opps number not found in the list ")
        