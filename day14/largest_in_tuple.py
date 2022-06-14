"""Defination:Program to Find Largest Item in a Tuple"""
def tuple_max(my_tuple):
    """Algorithm for lagest in tuple"""
    tuple_largest = my_tuple[0]
    for element in range(1, len(my_tuple)):
        if tuple_largest < my_tuple[element]:
            tuple_largest = my_tuple[element]
            largest_position = element
    print(f"Largest Item in mxTuple Tuple     = {tuple_largest}")
    print(f"Largest Tuple Item index Position = {largest_position}")
if __name__=='__main__':
    MY_TUPLE=input("Enter the number with comma seperated: \n")
    MY_TUPLE=tuple(int(x) for x in MY_TUPLE.split(","))
    print(f"The given tuple is : \n {MY_TUPLE}")
    tuple_max(MY_TUPLE)
