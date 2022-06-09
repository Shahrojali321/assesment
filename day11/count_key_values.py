"""Defination:Program to count the Number of occurrences of a key-value pair in a text
file"""
def count_keys(file):
    """algorithm to count occurance of keys"""
    dictonary = dict()
    for res in file:
        res = res.strip()
        res = res.lower()
        lines = res.split()
        for line in lines:
            if line in dictonary:
                dictonary[line] = dictonary[line]+1
            else:
                dictonary[line] = 1
    file.close()
    for key in list(dictonary.keys()):
        print("{} : {}".format(key,dictonary[key]))
if __name__=='__main__':
    FILE = open("d:/pratice/pramods_code/new_module/day11/count.txt", "r")
    count_keys(FILE)
