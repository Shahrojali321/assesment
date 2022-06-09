"""Defination:Program for Find sum of even factors of a numbers"""
def even_factor_sum(number):
    """algorithm for even factor sum"""
    summation=0
    for i in range(1,number+1):
        if number%i==0 and i%2==0:
            summation=summation+i
    return summation
if __name__=='__main__':
    NUMBER=int(input("Enter the number: "))
    result= even_factor_sum(NUMBER)
    print(f"The even factor sum of number is : {result}")
            