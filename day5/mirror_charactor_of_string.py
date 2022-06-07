"""Defination:find mirror characters in a string"""
import string
def mirror(given_string):
    """function for reversing the string"""
    alphabet=string.ascii_lowercase
    reverse=alphabet[::-1]
    dictonary=dict(zip(alphabet,reverse))
    # slicing the string after which it is going to reverse 
    prefix=given_string[:position]
    suffix=given_string[position:]
    mirror_part=""
    #for reversing the alphabet
    for char in suffix:
        mirror_part= mirror_part + dictonary[char]
    mirror_word=prefix+mirror_part
    return mirror_word
if __name__=='__main__':
    GIVEN_STRING=input("Enter the string: ")
    position=int(input("enter the position after which you want to reverse:"))
    print(f"The reversed string after n'th position is : {mirror(GIVEN_STRING)}")
