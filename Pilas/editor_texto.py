from pynput import keyboard as kb

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self, max_size = -1):
        self.head = None
        self.size = 0
        self.max_size = max_size

    def is_empty(self):
        return self.head is None

    def push(self, data):
        if self.max_size == self.size:
            return
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

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

n = int(input("Cuantos datos desea tener en el historial? "))

history = Stack() if n < 1 else Stack(n)

def press(key):
    if(key == kb.KeyCode.from_char('\x1a')):
        old_value = "" if history.is_empty() else history.pop()
        print(old_value, end = "")
        return
    
    if key in [kb.Key.shift, kb.Key.shift_r, kb.Key.shift_l, kb.Key.ctrl, kb.Key.ctrl_r, kb.Key.ctrl_l]:
        return
    if key in [kb.Key.backspace]:
        return
    
    key = " " if key == kb.Key.space else str(key).strip("'")
    print(key, end = "")
    history.push(key)

with kb.Listener(press) as listener:
    listener.join()