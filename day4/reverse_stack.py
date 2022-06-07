"""Defination: Program to Reverse a Stack using Recursion"""
from collections import deque
stack=[]
"""Recursive function to insert an item at the bottom of a given stack"""
def insertAtBottom(mystack, item):
    if not mystack:
        mystack.append(item)
        return
    top = mystack.pop()
    insertAtBottom(mystack, item)
    mystack.append(top)
def reverse_stack(mystack):
    """Recursive function to reverse a given stack"""
    if not mystack:
        return
    item = mystack.pop()
    reverse_stack(mystack)
    insertAtBottom(mystack, item)
if __name__=='__main__':
    #creating given stack from user
    stack_length=int(input("Enter the size of stack: "))
    for element in range(0,stack_length):
        element=input("Enter the element of a list: ")
        stack.append(element)
    MY_STACK= deque(stack)
    print(f'Original stack is: {MY_STACK}')
    reverse_stack(MY_STACK)
    print(f'Reversed stack is: {MY_STACK}')
