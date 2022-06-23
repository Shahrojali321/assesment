"""Defination: Python program to find the number of triplet whose summantion is zero"""
def triplet_sum(my_list):
    """Algorithm to find number of triplet"""
    count=0
    for i in my_list:
        for j in my_list:
            for k in my_list:
                summation=i+j+k
                if summation==0:
                    count=count+1
    return count
if __name__=='__main__':
    MY_LIST=[]
    LIST_LENGTH=int(input("Enter the length of list: "))
    for element in range(LIST_LENGTH):
        elements=int(input("Enter the numbers in list: "))
        MY_LIST.append(elements)
    print(f"The number of truplet whose summation is zero : \n {triplet_sum(MY_LIST)}")
