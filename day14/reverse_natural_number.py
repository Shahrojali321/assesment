"""Defination: Program to Print Natural Numbers in Reverse Order"""
def number_reverse(number):
    """algorithm to print natural number in reverse"""
    for num in range(number,0,-1):
        print(num,end=' ')
if __name__=='__main__':
    NUMBER=int(input("Enter the last term of natural number: "))
    number_reverse(NUMBER)
    