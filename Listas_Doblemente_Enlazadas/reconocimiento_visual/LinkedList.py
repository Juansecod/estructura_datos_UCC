class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None
        self.current = None
    
    def is_empty(self):
        return self.head is None
    
    def append(self, data):
        new_node =  Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            last_node = self.current
            new_node.prev = last_node
            last_node.next = new_node
        
        self.last = new_node
        self.current = new_node
            
    def display(self):
        if self.is_empty():
            return
        nodo = self.head
        while nodo.next != None:
            print(nodo.data)
            nodo = nodo.next
        print(nodo.data)