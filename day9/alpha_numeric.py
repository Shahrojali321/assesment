"""Defination: Program to accept string ending with alphanumeric character"""
import re
def check_string(my_string):
    """algorithm to accept the string ending with alphanumeric character"""
    if(re.search(REGEX_EXPRESSION, my_string)):
        print("The string ends with alphanumeric character")
    else:
        print("The string doesnot end with alphanumeric character")
if __name__=='__main__':
    REGEX_EXPRESSION = '[a-zA-z0-9]$'
    TEST_STRING=input("Enter the string : ")
    print(f"Your string is: \n {TEST_STRING}")
    check_string(TEST_STRING)
