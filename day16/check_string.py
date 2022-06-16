"""Defination :Check whether a string starts and ends with the same character or not"""
import re
def check_string(test_string,regex):
    """Algorithm to check string """
    if re.search(regex, test_string):
        print("Valid String")
    else:
        print("Invalid String")
if __name__=='__main__':
    REGEX = r'^[a-z]$|^([a-z]).*\1$'
    TEST_STRING=input("Enter the string: ")
    check_string(TEST_STRING,REGEX)
