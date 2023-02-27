# Listas enlazadas

Una lista enlazada es una estructura de datos en la que cada elemento de la lista está representado por un objeto llamado `Nodo`. Cada nodo contiene dos partes principales: una parte que almacena los datos (el elemento en sí mismo) y otra parte que almacena la referencia al siguiente nodo de la lista. La referencia al siguiente nodo se conoce como `enlace` o `puntero`.

La lista enlazada se compone de un conjunto de nodos en los que cada uno de ellos apunta al siguiente, formando así una secuencia de elementos. La lista enlazada tiene un nodo inicial, conocido como `cabeza` o primer nodo, y un nodo final, conocido como `cola` o último nodo.

La principal ventaja de la lista enlazada sobre otras estructuras de datos, como los arrays(arreglos), es que se pueden insertar o eliminar elementos de manera eficiente en cualquier posición de la lista. En una lista enlazada, para insertar un nuevo nodo, basta con modificar el puntero del nodo anterior para que apunte al nuevo nodo y el puntero del nuevo nodo para que apunte al siguiente nodo en la lista. De manera similar, para eliminar un nodo, solo es necesario modificar los punteros del nodo anterior y del siguiente para que apunten uno al otro, eliminando así el nodo intermedio.

Una variante de la lista enlazada es la lista doblemente enlazada, en la que cada nodo contiene también una referencia al nodo anterior. Esto permite la eliminación e inserción de elementos en ambas direcciones con la misma eficiencia.

## ¿Que algoritmo de ordenamiento usar en una lista enlazada?

Los algoritmos de ordenamiento que se usan para una lista enlazada son diferentes a los que se usan para un arreglo.

Para una lista enlazada, el algoritmo de ordenamiento más utilizado es el algoritmo de ordenamiento por `selección (Selection Sort)` o el algoritmo de ordenamiento por `inserción (Insertion Sort)`.

El algoritmo de ordenamiento por selección para listas enlazadas funciona de la siguiente manera: se recorre la lista y se busca el elemento más pequeño en la lista, se intercambia con el primer elemento de la lista y se repite el proceso para el resto de la lista, colocando los elementos en su posición correcta.

El algoritmo de ordenamiento por inserción para listas enlazadas también funciona de manera similar a la versión para arreglos: se toma el primer elemento de la lista como una lista ordenada y se va insertando el siguiente elemento en la posición correcta dentro de esa lista ordenada.

Es importante mencionar que ambos algoritmos tienen una complejidad temporal de O(n^2), lo que los hace menos eficientes que los algoritmos de ordenamiento de división y conquista como Quicksort, Mergesort o Heapsort. Sin embargo, en el caso de listas enlazadas, no es tan sencillo aplicar los algoritmos de ordenamiento de división y conquista debido a la forma en que se almacenan los elementos en memoria.

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
    def delete(self, data):
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
    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.dato)
        current_node = current_node.next
    ```

## Ejercicio 1

Realiza los siguientes metodos para la clase `ListaEnlazada`:

- [x] **`buscar`:** Busca un dato en los nodos de la lista enlazada que devuelva un booleano, sera False en caso de que no se encuentre en ningun nodo.
- [x] **`tamaño`:** Devuelve la cantidad de nodos que tiene la lista enlazada
- [x] **`ordenar`:** Ordena de manera ascendente los nodos que tiene la lista enlazada
- [ ] **`invertir`:** Invierte el orden de los nodos de la lista enlazada

## Ejercicio 2

- [x] Crear una clase `Animal` con los métodos y atributos básicos. En uno de los atributos, debes indicar la edad y el tipo de animal (Águila, pantera, vaca, ...)

- [x] Crear una `lista enlazada` que permita agregar animales al listado, donde al momento de agregar un nuevo animal a la lista, esta no debe repetirse.

- [x] Para mostrar los animales que contiene la lista enlazada, debes realizarla usando dos métodos

  - [x] Una función recursiva
  - [x] Un bucle
