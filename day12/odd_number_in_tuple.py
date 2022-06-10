"""Defination:Program to Print Odd Numbers in Tuple"""
def odd_number(given_tuple):
    """Algorithm to get odd from tuple"""
    for number in range(len(given_tuple)):
        if given_tuple[number]%2!=0:
            print(given_tuple[number],end=" ")
if __name__=='__main__':
    MY_TUPLE=input("Enter the number with comma seperated: \n")
    MY_TUPLE=tuple(int(x) for x in MY_TUPLE.split(","))
    print(f"The given tuple is : \n {MY_TUPLE}")
    print("The odd number in tuple are:")
    odd_number(MY_TUPLE)
