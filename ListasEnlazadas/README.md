# Listas enlazadas

Una lista enlazada es una estructura de datos en la que cada elemento de la lista está representado por un objeto llamado `Nodo`. Cada nodo contiene dos partes principales: una parte que almacena los datos (el elemento en sí mismo) y otra parte que almacena la referencia al siguiente nodo de la lista. La referencia al siguiente nodo se conoce como `enlace` o `puntero`.

La lista enlazada se compone de un conjunto de nodos en los que cada uno de ellos apunta al siguiente, formando así una secuencia de elementos. La lista enlazada tiene un nodo inicial, conocido como `cabeza` o primer nodo, y un nodo final, conocido como `cola` o último nodo.

La principal ventaja de la lista enlazada sobre otras estructuras de datos, como los arrays(arreglos), es que se pueden insertar o eliminar elementos de manera eficiente en cualquier posición de la lista. En una lista enlazada, para insertar un nuevo nodo, basta con modificar el puntero del nodo anterior para que apunte al nuevo nodo y el puntero del nuevo nodo para que apunte al siguiente nodo en la lista. De manera similar, para eliminar un nodo, solo es necesario modificar los punteros del nodo anterior y del siguiente para que apunten uno al otro, eliminando así el nodo intermedio.

Una variante de la lista enlazada es la lista doblemente enlazada, en la que cada nodo contiene también una referencia al nodo anterior. Esto permite la eliminación e inserción de elementos en ambas direcciones con la misma eficiencia.

## Metodos en las listas enlazadas

- **`Constructor`:** Creación de la lista enlazada
    ```py
    def __init__(self):
        self.head = None
    ```
- **`es_vacio`:** Devuelve un boolean que es True si la lista esta vacia
    ```py
    def is_empty(self):
        return self.head is None
    ```
- **`agregar_nodo`:** Agrega un nodo en la ultima posición de la lista
    ```py
    def push(self, data):
        current_node = Node(data)
        if self.es_vacio():
            self.cabeza = node
        else:
            current_node = self.cabeza
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = node
    ```
- **`eliminar`:** Elimina el elemento de la lista enlazada
    ```py
    def eliminar(self, data):
      current_node = self.head
      if current_node.data == data:
          self.head = current_node.next
          return
      while current_node.next is not None:
          if current_node.next.data == data:
              current_node.next = current_node.next.next
              return
          current_node = current_node.next
    ```
- **`imprimir_lista`:** Imprime los datos de cada nodo de la lista
    ```py
    def imprimir(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.dato)
        current_node = current_node.next
    ```

# Ejercicio

Realiza los siguientes metodos para la clase `ListaEnlazada`:
- [x] **`buscar`:** Busca un dato en los nodos de la lista enlazada que devuelva un booleano, sera False en caso de que no se encuentre en ningun nodo.
- [x] **`tamaño`:** Devuelve la cantidad de nodos que tiene la lista enlazada
- [ ] **`ordenar`:** Ordena de manera ascendente los nodos que tiene la lista enlazada
- [ ] **`invertir`:** Invierte el orden de los nodos de la lista enlazada
