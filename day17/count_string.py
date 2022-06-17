"""Defination: Program to Count Total Characters in a String"""
def count_string(string):
    """Algorithm to count string characters"""
    count=0
    for char in string:
        count=count + 1
    return count
if __name__=='__main__':
    STRING=input("Enter the string: ")
    print(f"The number of characters in string is: \n {count_string(STRING)}")
