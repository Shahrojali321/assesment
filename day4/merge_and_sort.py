"""Defination:Program to Merge Two Lists and Sort it."""
def sort_merge_lst(list1,list2):
    """function to merge and sort the list"""
    merge_lst=list1+list2
    merge_lst.sort()
    return merge_lst
if __name__=='__main__':
    LIST1=[]
    LIST2=[]
    #creating the two list to be merge
    list1_size=int(input("Enter the size of list1: "))
    for element in range(0,list1_size):
        element=int(input("Enter the Elements of the list1: "))
        LIST1.append(element)
    list2_size=int(input("Enter the size of list1: "))
    for element in range(0,list2_size):
        element=int(input("Enter the Elements of the list2: "))
        LIST2.append(element)
    RESULT=sort_merge_lst(LIST1,LIST2)
    print(f"The sorted merge list is: {RESULT}")
