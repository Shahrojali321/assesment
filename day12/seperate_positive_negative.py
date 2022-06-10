"""Defination:"""
def seperate_list(list1):
    """algorithm to seperate positive and negative"""
    positive_list=[]
    negative_list=[]
    for number in list1:
        if number>=0:
            positive_list.append(number)
        else:
            negative_list.append(number)
    print(f"The positive number list is : \n {positive_list}")
    print(f"The negative number list is : \n {negative_list}")
if __name__=='__main__':
    LIST1=[]
    list_length=int(input("Enter the length of list: "))
    for element in range(0,list_length):
        element=int(input("Enter the number in list: "))
        LIST1.append(element)
    print(f"The original list is : \n {LIST1}")
    seperate_list(LIST1)
