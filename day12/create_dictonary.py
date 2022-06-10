"""Defination:Python Program to Create Dictionary of Numbers 1 to n in (x, x*x) form"""
def create_dictonary(maximum):
    """Algorithm to for dictonary of square of numbers """
    my_dictonary={}
    for number in range(1,maximum+1):
        my_dictonary[number]=number*number
    return my_dictonary
if __name__=='__main__':
    MAXIMUM=int(input("Enter the maximum number: "))
    print(f"Dictonary: \n {create_dictonary(MAXIMUM)}")
