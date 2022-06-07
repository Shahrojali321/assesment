"""Defination:Program which iterates the integers from 1 to 50"""
def muntiple(num):
    """Algorithm to iterates the integer"""
    for i in range(1,num+1):
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
if __name__=='__main__':
    LAST_NUMBER=int(input("Enter the last number of series: "))
    result=muntiple(LAST_NUMBER)
