"""Defination: Program to Perform Singly Linked List Operations"""
class Node(object):
    """for node"""
    def __init__ (self, data, node = None):
        self.data = data
        self.next_node = node
    def get_next (self):
        """for next node"""
        return self.next_node
    def set_next (self, node):
        """set next"""
        self.next_node = node
    def get_data (self):
        """setting data """
        return self.data
    def set_data (self, data):
        """to set the data"""
        self.data = data

class LinkedList (object):
    """for operation"""
    def __init__(self, root_node = None):
        self.root = root_node
        self.size = 0
    def get_size (self):
        """To get size of the list"""
        return self.size
    def add (self, data):
        """Add in the list"""
        new_node = Node (data, self.root)
        self.root = new_node
        self.size += 1
    def remove (self, data):
        """to remove form the list"""
        this_node = self.root
        prev_node = None
        while this_node:
            if this_node.get_data() == data:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False
    def find (self, data):
        """to find the element"""
        this_node = self.root
        while this_node:
            if this_node.get_data() == data:
                return data
            else:
                this_node = this_node.get_next()
        return None
if __name__=='__main__':
    myList = LinkedList()
    myList.add(5)
    myList.add(8)
    myList.add(12)
    print("size="+str(myList.get_size()))
    myList.remove(8)
    print("size="+str(myList.get_size()))
    print(myList.remove(12))
    print("size="+str(myList.get_size()))
    print(myList.find(5))
