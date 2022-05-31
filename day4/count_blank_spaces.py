"""Defination:Program to Count the Number of Blank Spaces in a Text File"""

file = open("d:/pratice/pramods_code/new_module/day3/file1.txt", "r")

"function to count spaces"
def count_space(file):  
    count = 0
    while True:
        char = file.read(1)
      
        if (char==" "):
            count += 1
        if not char:
            break
    return count
result=count_space(file)
print(f"The number of spaces in the file is: {result}")