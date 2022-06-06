"""Defination:Program to Sort the values of first list using second list"""
def sorting_of_element(list1,list2):
    """Algorithm to sort the list1 using list2"""
    dictonary = {}
    final_list = []
    # Addition of two list in one dictionary
    dictonary = {list1[i]: list2[i] for i in range(len(list2))}
    temp_dictonary = {k: v for k, v in sorted(dictonary.items(), key=lambda item: item[1])}
    for i in temp_dictonary.keys():
        final_list.append(i)
    return final_list
if __name__=='__main__':
    first_list = []
    second_list = []
    list_size=int(input("Enetr the lenth of 1st and 2nd list"))
    for element in range(0,list_size):
        element=input("Enter the Elements of the first_list: ")
        first_list.append(element)
    for element in range(0,list_size):
        element=int(input("Enter the Elements of the second_list: "))
        second_list.append(element)
    result=sorting_of_element(first_list,second_list)
    print(f"The sorted list is: {result}")
