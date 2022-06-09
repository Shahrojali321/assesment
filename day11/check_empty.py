"""Defination:Program to check if a string can become empty by recursive deletion"""
def check_empty(sub_string,given_string):
    """algorithm to for recursive deletion"""
    while len(given_string)!=0:
        try:
            sub_string_index=given_string.index(sub_string)
        except ValueError:
            return 'false'
        given_string=given_string[:sub_string_index]+given_string[sub_string_index+len(sub_string):]
        print(given_string)
    return 'true'
if __name__=='__main__':
    GIVEN_STRING=input("Enter the test string: ")
    SUB_STRING=input("Enter the substring : ")
    print(check_empty(SUB_STRING,GIVEN_STRING))
