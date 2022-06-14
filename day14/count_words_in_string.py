"""Defination:Program to Count Total Number of Words in a String"""
def count_words(string):
    """algorithm to count words in string"""
    words=string.split()
    count=0
    for word in words:
        count=count+1
    return count
if __name__=='__main__':
    STRING=input("Enter the string: \n ")
    print(f"The total number of words is : \n {count_words(STRING)}")
