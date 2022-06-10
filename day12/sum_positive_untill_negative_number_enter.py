"""Defination:Python Program to Find Sum of 10 Numbers until user enters Positive Numbers"""
if __name__=="__main__":
    SUMMATION=0
    for element in range(1,11):
        number=int(input("Enter the number: "))
        if number<0:
            break
        SUMMATION=SUMMATION+number
    print(f"The sum is : {SUMMATION}")
    