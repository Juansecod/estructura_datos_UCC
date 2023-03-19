class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
    
    def is_empty(self):
        return self.first is None
    
    def append(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.first = new_node
        else:
            self.last.next = new_node
        self.last = new_node
    
    def pop(self):
        if self.is_empty():
            return None
        value = self.first.value
        self.first = self.first.next
        if self.first is None:
            self.last = None
        return value
    
    def display(self):
        if self.is_empty():
            print("The Queue is empty...")
        current = self.first
        while current:
            print(current.value, end=f"\n\n")
            print("-"*150)
            current = current.next

    def size(self):
        if self.is_empty():
            return 0
        current = self.first
        cont = 0
        while current:
            cont += 1
            current = current.next
        return cont