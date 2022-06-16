"""Defination: Python Program to Print Floyds Triangle using For Loop"""
def floyds_traingle(rows):
    """Algorithm to print floyds traingle"""
    num=1
    for row in range(rows):
        for j in range(row+1):
            print(num,end=' ')
            num=num+1
        print()
if __name__=='__main__':
    ROWS=int(input("Enter the number of rows: "))
    floyds_traingle(ROWS)
