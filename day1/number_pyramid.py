"""Defination:to find the number pattern """
def patt(row):
    k=1
    i=1
    while i<=row:
        b=1
        while b<=row-i:
            print(" ",end=" ")
            b=b+1
        j=1
        while j<=k:
            print(i,end=" ")
            j=j+1
        k=k+2
        print()
        i=i+1
row=int(input("enter the number of rows: "))
result=patt(row)