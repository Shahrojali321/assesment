"""Defination:Program to find ASCII Value of Total Characters in a String"""
def ascii_value(string):
    """Algorithm for ASCII value"""
    for i in range(len(string)):
        print("The ASCII Value of Character %c = %d" %(string[i], ord(string[i])))
if __name__=='__main__':
    STRING=input("Enter the String: \n ")
    ascii_value(STRING)
