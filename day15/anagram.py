"""Defination: Print anagrams together in Python using List and Dictionary"""
def anagram_group(list1):
    """Algorithm to print anagrams"""
    dictionary={}
    for word in list1:
        sorted_word = "".join(sorted(word))
        if sorted_word not in dictionary:
            dictionary[sorted_word]=[word]
        else:
            dictionary[sorted_word].append(word)
    result=[]
    for items in dictionary.values():
        result.append(items)
    return result
if __name__=='__main__':
    LIST1=input("Enter the string: ")
    LIST1=LIST1.split(" ")
    print(LIST1)
    print(f"The amalgum goup : \n {anagram_group(LIST1)}")
