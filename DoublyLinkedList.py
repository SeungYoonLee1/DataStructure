class DoublyLinkedList:
  
    class EmptyError(Exception):
        pass
    
    class Node:
        def __init__(self, data, prev = None, next = None):
            self.data = data
            self.prev = None
            self.next = None
            
    def __init__(self):
        # Create head node, tail node as dummy(None) node
        self.head = self.Node(None)
        self.tail = self.Node(None)
        self.size = 0
        
    def insert_after(self, p, data): # p is the node we want to insert after
        new_node = self.Node(data)
        if self.list_size() == 0: # Node dosen't exist in the list
            self.head.next = new_node
            self.tail.prev = new_node
            new_node.prev = self.head
            new_node.next = self.tail
        else: # Node exists in the list
            new_node.prev = p
            new_node.next = p.next
            p.next.prev = new_node
            p.next = new_node
        self.size += 1
        
    def insert_before(self, p, data):
        new_node = self.Node(data)
        if self.list_size() == 0:
            self.head.next = new_node
            self.tail.prev = new_node
            new_node.prev = self.head
            new_node.next = self.tail
        else:
            new_node.prev = p.prev
            new_node.next = p
            p.prev.next = new_node
            p.prev = new_node
        self.size += 1
        
    def delete(self, p): # p is the node we want to delete
        if self.list_size() == 0:
            print('There is not Node to delete')
            raise(EmptyError)
        p.prev.next = p.next
        p.next.prev = p.prev
        self.size -= 1
        return p
        
    def list_size(self): return self.size
    
    def print_list(self):
        if self.size == 0:
            print('Empty List')
            return
        p = self.head.next
        while p != self.tail:
            if p.next != self.tail:
                print(p.data, ' <=> ' ,end ='')
            else:
                print(p.data)
            p = p.next
        
