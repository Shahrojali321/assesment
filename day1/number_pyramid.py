"""Defination:to find the number pattern """
def patt(row):
    """algorithm of number pattern"""
    digit_range=1
    digit=1
    while digit<=row:
        gap=1
        while gap<=row-digit:
            print(" ",end=" ")
            gap=gap+1
        j=1
        while j<=digit_range:
            print(digit,end=" ")
            j=j+1
        digit_range=digit_range+2
        print()
        digit=digit+1
if __name__=='__main__':
    RAW=int(input("enter the number of rows: "))
    patt(RAW)
    