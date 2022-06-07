"""Defination:Program to read contents and copy only the content of odd lines into new file"""
def copy_in_new_file(my_file,new_file):
    """
    reading lines on exiting file and write in a new file
    """
    lines=my_file.readlines()
    for count_line in range(len(lines)):
        if(count_line%2==0):
            new_file.write(lines[count_line])
        else:
            pass
    new_file.close()
    new_file=open('file3.txt','r')
    new_file1=new_file.read()
    new_file.close()
    my_file.close()
    return new_file1
if __name__=='__main__':
    MY_FILE = open('d:/pratice/pramods_code/new_module/day5/file2.txt','r')
    NEW_FILE=open('file3.txt','w')
    print(f"{copy_in_new_file(MY_FILE,NEW_FILE)}")
