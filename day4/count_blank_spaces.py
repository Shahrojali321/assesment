"""Defination:Program to Count the Number of Blank Spaces in a Text File"""
file=open("d:/pratice/pramods_code/new_module/day3/file1.txt", "r")
def count_space(file):
    """function to count spaces"""
    count = 0
    while True:
        char = file.read(1)
        if (char==" "):
            count += 1
        if not char:
            break
    return count
if __name__=='__main__':
    RESULT=count_space(file)
    print(f"The number of spaces in the file is: {RESULT}")
    