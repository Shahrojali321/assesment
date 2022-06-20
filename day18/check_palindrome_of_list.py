"""Defination:check if the given linked list is palindrome or not"""
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
def check_palindrome(left, right):
    """Recursively to check the palindrome"""
    if right is None:
        return True, left
    val, left = check_palindrome(left, right.next)
    result = val and (left.data == right.data)
    left = left.next
    return result, left
def palindrome(head):
    """to check palindrome"""
    return check_palindrome(head, head)[0]
if __name__ == '__main__':
    KEYS = [1, 3, 5, 3, 1]
    HEAD = None
    for i in reversed(range(len(KEYS))):
        HEAD = Node(KEYS[i], HEAD)
    if palindrome(HEAD):
        print('\n \n \n The linked list is a palindrome \n \n \n ')
    else:
        print('\n \n \n The linked list is not a palindrome \n \n \n ')
