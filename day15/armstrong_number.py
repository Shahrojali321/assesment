"""Defination:Program to check Armstrong Number"""
def angstrom(number):
    """Algorithm for armstron number"""
    summation=0
    temp=number
    while number>0:
        digit=number%10
        summation=summation+digit*digit*digit
        number=number//10
    if summation==temp:
        print("It is a Angstrom number")
    else:
        print("It is not a Angstrom number")
if __name__=='__main__':
    NUMBER=int(input("Enter the number: \n "))
    angstrom(NUMBER)
