class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
class Stack:
    def __init__(self):
        self.head = None
 
    def is_empty(self):
        return self.head is None
 
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
 
    def pop(self):
        if self.is_empty():
            return None
        popped_node = self.head
        self.head = self.head.next
        popped_node.next = None
        return popped_node.data
 
    def peek(self):
        if self.is_empty():
            return None
        return self.head.data
 
    def display(self):
        current = self.head
        while current:
            print(current.data, end='->')
            current = current.next
        print()
  
stack = Stack()       
        
# Apilamos los datos dentro de la pila
stack.push("Primer Elemento")
stack.push("Segundo Elemento")
stack.push("Tercero Elemento")
stack.push("Cuarto Elemento")

# Mostramos el dato que esta en la cabeza 
print("Primer dato en salir:")
print(stack.peek())
print("-"*50)

# Mostramos todos los datos que hay dentro de la pila 
print("Elementos de la pila: ")
stack.display()
print("-"*50)

# Desapilamos dos elementos 
stack.pop()
stack.pop()

# Mostramos la pila ahora con los elementos desapilados
print("Elementos de la pila luedo de desapilarla dos veces: ")
stack.display()
print("-"*50)