"""Defination: Program for Print Number series without using any loop """
def number_series(number,variable,flag,common_difference):
    """Algorithm of number series """
    print(number, end=' ')
    if (number<=0):
        if (flag==0):
            flag=1
        else:
            flag=0
    if (number==variable and (not(flag))):
        return
    if (flag==True):
        number_series(number-common_difference,variable,flag,common_difference)
        return
    if (not(flag)):
        number_series(number+common_difference,variable,flag,common_difference)
        return
if __name__=='__main__':
    NUMBER=int(input("Enter the last number of series: "))
    COMMON_DIFFERENCE=int(input("Enter the common_diffence: "))
    number_series(NUMBER,NUMBER,True, COMMON_DIFFERENCE)
