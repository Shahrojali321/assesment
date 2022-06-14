"""Defination:Program to Count words in a String using Dictionary"""
def count_word(string):
    """Algorithm to count words using dictionary"""
    words=[]
    my_dictionary={}
    words=string.split()
    for key in words:
        my_dictionary[key]= words.count(key)
    print(f"Dictionary of words : \n {my_dictionary}")
if __name__=='__main__':
    STRING=input("Enter the string: \n")
    count_word(STRING)
