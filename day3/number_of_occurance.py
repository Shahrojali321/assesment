"""Defination:Program that Reads a Text File and Counts Certain Letter Appears in the Text File"""
def letter_count(file1, letter):
    """For count the letter in file"""
    file = open(file1, 'r')
    for line in file:
        line=line.strip()
        line=line.lower().replace(".","")
        word=line.split()
    print(word)
    count=0
    for count_letter in word:
        if count_letter==letter:
            count=count+1
    return count
if __name__=='__main__':
    LETTER=input("Enter the letter which you want to count: ")
    RESULT=letter_count('d:/pratice/pramods_code/new_module/day3/file1.txt', LETTER)
    print(f"Number of times the letter found in file is: {RESULT}")
