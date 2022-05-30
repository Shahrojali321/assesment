"""Defination: program which iterates the integers from 1 to 50"""
def muntiple(n):
    for i in range(1,n+1):
        if (i%3==0 and i%5!=0):
            i='Maple' 
        elif(i%5==0 and i%3!=0):
            i='labs' 
        elif(i%3==0 and i%5==0):
            i='Maplelabs' 
        else:
            i=i
        print(i)
    print()
    return i
n=int(input("Enter the last number of series: "))
result=muntiple(n)
