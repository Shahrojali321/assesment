"""Defination:Program to Merge Two Lists and Sort it."""
list1=[]
list2=[]
"function to merge and sort the list"
def sort_merge_lst(list1,list2):
    merge_lst=list1+list2
    merge_lst.sort()
    return merge_lst
    
"""creating the two list to be merge """
list1_size=int(input("Enter the size of list1: "))
for element in range(0,list1_size):
    element=int(input("Enter the Elements of the list1: "))
    list1.append(element)
list2_size=int(input("Enter the size of list1: "))
for element in range(0,list2_size):
    element=int(input("Enter the Elements of the list2: "))
    list2.append(element)

result=sort_merge_lst(list1,list2)
print(f"The sorted merge list is: {result}")