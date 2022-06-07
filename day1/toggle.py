"""Defination: To convert toggle string."""
def tog(string):
    """Algorithm goggle string"""
    string1 = ''
    for i in string:
        if('a'<= i <= 'z'):
            string1 = string1 + chr((ord(i) - 32))
        elif('A'<= i <= 'Z'):
            string1 = string1 + chr((ord(i) + 32))
        else:
            string1 = string1 + i
    return string1
if __name__=='__main__':
    STRING = input("Please Enter your Own String : ")
    result=tog(STRING)
    print(f"\nOriginal String                      =  {STRING}")
    print(f"The Given String After Toggling Case =  {result}")
