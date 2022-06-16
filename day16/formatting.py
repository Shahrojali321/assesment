"""Program to Print Tuple using string formatting"""
if __name__=='__main__':
    MY_LIST=[]
    LIST_LENGTH=int(input("Enter the length of tuple: "))
    for element in range(LIST_LENGTH):
        elements=int(input("Enter the element of tuple: "))
        MY_LIST.append(elements)
    MY_TUPLE=tuple(MY_LIST)
    print(f"The Tuple is : {format(MY_TUPLE)}")
