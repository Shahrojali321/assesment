"""Defination:Python program to Check if Binary representation is Palindrome or not"""

def check_binary_pelindrome(number):
    """function to check the pelindrome of binary representation"""
    binary=bin(number)
    binary=binary[2:]
    temp=binary[-1::-1]
    if(temp==binary):
        print(f"True \n Binary representation of number={number} is {binary} which is palindrome as well")
    else:
        print(f"False \n Binary representation of number={number} is {binary} which is not palindrome ")
    return
if __name__=='__main__':
    number=int(input("enter the number: "))
    check_binary_pelindrome(number)
