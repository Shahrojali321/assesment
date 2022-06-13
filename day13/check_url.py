"""Defination:Check if an URL is valid or not using Regular Expression"""
import re
def check_url(url):
    """algorithm to check the url"""
    regex = ("((http|https)://)(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")
    pattern = re.compile(regex)
    if url is None:
        return False
    if re.search(pattern,url):
        return True
if __name__=='__main__':
    URL =input("Enter the url")
    if check_url(URL) is True:
        print("Yes the url is correct")
    else:
        print("No the url is not correct")
