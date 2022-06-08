"""defination:Python Program to find Strong Number using While Loop"""
def strong_number(number):
    """Algorithm for strong number"""
    summation=0
    temp=number
    while 0<temp:
        factorial=1
        remainder=temp % 10
        for i in range(1,remainder+1):
            factorial=factorial*i
        summation=summation+factorial
        temp=temp//10
    if summation==number:
        print(f"The number {number} is strong number")
    else:
        print(f"The number {number} is not strong number")
if __name__=='__main__':
    NUMBER=int(input("Enter the number : "))
    strong_number(NUMBER)
