from pandas import DataFrame
import requests
import threading
from os import system

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
            current = current.next
        print("-"*100)    

urls = Queue()
responses = Queue()

def fetch(url):
    r = requests.get(url)
    df = DataFrame(r.json())
    responses.append(df)
    system("cls")
    urls.display()
    responses.display()

threads = []
for url in ["http://localhost:8000/productos", "http://localhost:8000/carts", "http://localhost:8000/users", ]:
    urls.append(url)
    thread = threading.Thread(target=fetch, args=[url])
    threads.append(thread)

for f in threads:
    f.start()
