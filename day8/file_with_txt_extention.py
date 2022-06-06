"""Defination:To find the file of particular extension"""
import os
def file_name(directory):
    """To find the file of particular extension"""
    files_present=[]
    for filename in os.listdir(directory):
        if not filename.endswith('.txt'):
            continue
        files_present.append(filename)
    return files_present
if __name__=='__main__':
    PATH = 'D:/pratice/module01/XML'
    #pattern=input("Enter the type of file you want:")
    result=file_name(PATH)
    print(f" The file is : \n{result}")
