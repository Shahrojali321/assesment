"""Defiantion:Program to count characters frequency in a string using for loop and dictionary"""
def char_frequency(str1):
    """algorithm to count charactor in string"""
    dictonary = {}
    for charactor in str1:
        keys = dictonary.keys()
        if charactor in keys:
            dictonary[charactor] += 1
        else:
            dictonary[charactor] = 1
    return dictonary
if __name__=='__main__':
    TEST_STRING=input("Enter the string: ")
    print(char_frequency(TEST_STRING))
