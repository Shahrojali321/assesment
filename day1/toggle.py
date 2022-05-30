"""Defination: To convert toggle string."""
def tog(string):
    string1 = ''
    for i in string:
        if(i >= 'a' and i <= 'z'): 
            string1 = string1 + chr((ord(i) - 32)) 
        elif(i >= 'A' and i <= 'Z'):
            string1 = string1 + chr((ord(i) + 32))
        else:
            string1 = string1 + i
    return string1
string = input("Please Enter your Own String : ")
result=tog(string) 
print(f"\nOriginal String                      =  {string}")
print(f"The Given String After Toggling Case =  {result}")