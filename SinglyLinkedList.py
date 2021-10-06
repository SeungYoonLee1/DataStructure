class myError(Exception): # Exception class inheritance
    pass

class SinglyLinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def insert_front(self, data): # Data from the new node is received as a parameter.
        if self.head is None:
            new_node = self.Node(data)
            self.head = new_node
            self.size += 1
            return
        new_node = self.Node(data)
        new_node.next = self.head # Have parameter next as self.head
        self.head = new_node
        self.size += 1
        
    def insert_after(self, data, p): # p is already exist node
        new_node = self.Node(data) # Create new node
        if p is self.tail:
            self.tail = new_node
        new_node.next = p.next # next assign
        p.next = new_node # next assing of the existing node
        self.size += 1
        
    def delete_front(self):
        if self.head is None:
            raise(myError)
            return -1
        tmp = self.head.data
        self.head = self.head.next
        self.size -= 1
        return tmp
    
    def delete_after(self, p): # p is already existing node
        if p is self.tail:
            raise(meyError)
            return -1
        tmp = p.next.data # for return, save value temporarily
        p.next = p.next.next
        self.size -= 1
        return tmp
        
    def list_size(self): return self.size
    
    def search(self, target):
        if self.head is None:
            print('Error, no list item')
            return -1
        tmp = self.head
        for i in range(self.size):
            if target == tmp.data:
                print(f'target is in {i}-th index')
                return i
        print(f'cannot find {target} value in this list')

    def print_list(self):
        if self.head is None:
            print("Error, no list item")
            return -1
        tmp = self.head
        print('head : ', end=' ')
        while tmp.next is not None:
            print(tmp.data, '->' ,end=' ')
            tmp = tmp.next
        if tmp.next is None:
            print(tmp.data, end= ' ')
        print(': tail')
