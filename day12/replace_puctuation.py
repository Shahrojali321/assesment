"""Defination:Program to Remove Punctuations from a String"""
def remove_punctuation(my_string):
    """algorithm to replace punctuation"""
    punctuation='!@#$%^&*()_-+={}[]|\:;",./?><'
    punctuation=punctuation + "'"
    print(punctuation)
    my_string.split()
    for char in my_string:
        if char in punctuation:
            my_string=my_string.replace(char,"")
        "".join(my_string)
    return my_string
if __name__=='__main__':
    MY_STRING=input("Enter the string: ")
    print(f"The original string is : \n {MY_STRING}")
    print(f"String after removing the punctuation is : {remove_punctuation(MY_STRING)}")
