"""Defination:Program for Difference between sums of odd and even digits"""
def difference(number):
    """Algorithm to get difference of add and even digit"""
    even=0
    odd=0
    while number!=0:
        remainder=number%10
        if number%2==0:
            even=even+remainder
        else:
            odd=odd+remainder
        number=number//10
    result=odd-even
    return result
if __name__=='__main__':
    NUMBER=int(input("Enter the number: "))
    print(f"The difference of odd and even digits is : \n {difference(NUMBER)}")
