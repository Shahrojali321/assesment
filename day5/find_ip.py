"""Defination: To find the ip address """
import re
def ip_address(char):
    """To find the ip address"""
    list1=[]
    for char in file:
        if pattern.search(char):
            list1.append(char)
        return list1

if __name__=='__main__':
    ADDRESS=0
    file=["10.10.10.10","0.0.0.0","153.10.0.10","abcd"]
    pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    print(f"The ip address is:{ip_address(ADDRESS)}")
