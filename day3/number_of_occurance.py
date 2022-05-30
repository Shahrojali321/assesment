"""Defination: Program that Reads a Text File and Counts the Number of Times a Certain Letter Appears in the Text File"""
def letter_count(file1, letter):
    """For count the letter in file"""
    file = open(file1, 'r')
    lst=[]
    for line in file:
        line=line.strip()
        line=line.lower().replace(".","")
        word=line.split()
    print(word)
    count=0
    for i in word:
        if i==letter:
            count=count+1
    return count
 
letter=input("Enter the letter which you want to count: ")
result=letter_count('d:/pratice/pramods_code/new_module/day3/file1.txt', letter)
print(f"Number of times the letter found in file is: {result}")