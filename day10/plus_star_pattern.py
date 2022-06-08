"""Defination:Program to Print Plus Star Pattern using a for loop"""
def pattern(rows):
    """algorithm to print plus pattern"""
    for i in range(1,2*rows):
        for j in range(1,2*rows):
            if (i==rows or j==rows):
                print("*",end='')
            else:
                print(" ",end='')
        print()
if __name__=='__main__':
    ROWS=int(input("enter the number of rows: "))
    pattern(ROWS)
        