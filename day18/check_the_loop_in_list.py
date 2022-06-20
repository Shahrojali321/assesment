"""Defination:Check if the linked list has a loop"""
class Node:
    """Defining node class """
    def __init__(self,d):
        self.data = d
        self.next = None
HEAD = None
def push(new_data):
    """To push the data"""
    global HEAD
    new_node = Node(new_data)
    new_node.next = HEAD
    HEAD=new_node
def detect_loop(h):
    """Algorithm to detect the loop"""
    global HEAD
    if HEAD is None:
        return False
    else:
        while HEAD is not None:
            if HEAD.data == -1:
                return True
            else:
                HEAD.data = -1
                HEAD = HEAD.next
        return False
if __name__=='__main__':
    push(1)
    push(2)
    push(3)
    push(4)
    push(5)
    HEAD.next.next.next.next.next = HEAD.next.next
    if detect_loop(HEAD):
        print("True")
    else:
        print("False")
