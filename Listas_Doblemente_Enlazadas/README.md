# Listas Doblemente Enlazadas

Este tipo de dato es muy similar a las listas enlazadas, en donde su principal diferencia esta en que las listas doblemente enlazadas cuentan con dos apuntadores, una para el nodo previo y otra para el nodo siguiente.

## Metodos en las listas doblemente enlazadas

- **`Constructor`:** Creación de la lista enlazada

    ```py
    def __init__(self):
        self.head = None
        self.last = None
        self.current = None
    ```

- **`es_vacio`:** Devuelve un boolean que es True si la lista esta vacia

    ```py
    def is_empty(self):
        return self.head is None
    ```

- **`agregar_nodo`:** Agrega un nodo en la ultima posición de la lista

    ```py
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
    ```

- **`eliminar`:** Elimina el elemento de la lista enlazada

    ```py
    def delete(self, data):
      current_node = self.head
      if current_node.data == data:
          self.head = current_node.next
          self.head.prev = None
          return
      elif self.last.data == data:
          self.last.prev.next = None
          return
          
      while current_node.next is not None:
          if current_node.next.data == data:
              current_node.next = current_node.next.next
              current_node.next.prev = current_node
              return
          current_node = current_node.next
    ```

- **`imprimir_lista`:** Imprime los datos de cada nodo de la lista

    ```py
    def display(self):
        if self.is_empty():
            return
        nodo = self.head
        while nodo.next != None:
            print(nodo.data, end=", ")
            nodo = nodo.next
        print(nodo.data)
    ```
