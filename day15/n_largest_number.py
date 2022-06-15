"""Defination:Program to find N largest elements from a list"""
def largest(list1,length):
    """Algorithm to get maximum number list """
    max_list=[]
    for number in range(0,length):
        maximum=0
        for element in range(0,list_length):
            if list1[element]>maximum:
                maximum=list1[element]
        list1.remove(maximum)
        max_list.append(maximum)
    return max_list
if __name__=='__main__':
    LIST1=[]
    list_length=int(input("Enter the length of list: "))
    for char in range(list_length):
        elements=int(input("Enter the element of original list: "))
        LIST1.append(elements)
    N=int(input("Enter the range of maximum list: \n "))
    print(f"The list of maximum number : \n {largest(LIST1,N)} ")
