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
  
"""Recursive function to reverse a given stack"""
def reverseStack(mystack):

    if not mystack:
        return
    item = mystack.pop()
    reverseStack(mystack)
    insertAtBottom(mystack, item)

"""creating given stack from user """
stack_length=int(input("Enter the size of stack: "))
for element in range(0,stack_length):
    element=input("Enter the element of a list: ")
    stack.append(element)

mystack= deque(stack)
print(f'Original stack is: {mystack}')
reverseStack(mystack)
print(f'Reversed stack is: {mystack}')