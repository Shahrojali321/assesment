"""Defination: Read List of Dictionaries from File in Python"""
def get_dictionary(text):
    """Algorithm to read dictionary"""
    dictionary = {}
    pairs = text.strip('{}').split(', ')
    for values in pairs:
        pair = values.split(': ')
        dictionary[pair[0].strip('\'\'\"\"')] = pair[1].strip('\'\'\"\"')
    return dictionary
if __name__=='__main__':
    try:
        file1 = open('d:/pratice/pramods_code/new_module/day13/file_dictonary.txt', 'rt')
        lines = file1.read().split('\n')
        for line in lines:
            if line != '':
                DICTIONARY = get_dictionary(line)
                print(f"The dictionaries are : \n {DICTIONARY}")
        file1.close()
    except ValueError as V:
        print("Something unexpected occurred!")
