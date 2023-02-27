class Nodo:
  def __init__(self, dato):
    self.dato = dato
    self.next = None

# It's a linked list that can add, remove, search, and sort nodes
class ListaEnlazada:
  def __init__(self):
    self.cabeza = None

  def es_vacio(self):
    return self.cabeza is None

  def agregar_nodo(self, dato):
    nodo = Nodo(dato)
    if self.es_vacio():
      self.cabeza = nodo
    else:
      nodo_actual = self.cabeza
      while nodo_actual.next is not None:
        nodo_actual = nodo_actual.next
      nodo_actual.next = nodo
  
  def eliminar(self, dato):
      nodo_actual = self.cabeza
      if nodo_actual.dato == dato:
          self.cabeza = nodo_actual.next
          return
      while nodo_actual.next is not None:
          if nodo_actual.next.dato == dato:
              nodo_actual.next = nodo_actual.next.next
              return
          nodo_actual = nodo_actual.next
          
  def imprimir(self):
    nodo_actual = self.cabeza
    while nodo_actual is not None:
      print(nodo_actual.dato)
      nodo_actual = nodo_actual.next

  def buscar(self, dato):
    nodo_actual = self.cabeza
    if nodo_actual.dato == dato:
        return True
    while nodo_actual is not None:
        if nodo_actual.dato == dato:
          return True
        nodo_actual = nodo_actual.next
    return False

  def tamano(self):
    if self.es_vacio():
      return 0
    else:
      contador = 1
      nodo_actual = self.cabeza
      while nodo_actual.next is not None:
        contador += 1
        nodo_actual = nodo_actual.next
      return contador
    

  def ordenar(self):
    if self.cabeza is None:
      return
    current = self.cabeza
    while current.next:
      min_node = current
      temp = current.next
      while temp:
        if min_node.dato > temp.dato:
            min_node = temp
        temp = temp.next
      current.dato, min_node.dato = min_node.dato, current.dato
      current = current.next
        
    

  def invertir(self):
    pass

lista = ListaEnlazada()

print("Agregamos datos al nodo")
lista.agregar_nodo(3)
lista.agregar_nodo(2)
lista.agregar_nodo(1)
lista.agregar_nodo(6)
lista.agregar_nodo(5)
lista.agregar_nodo(4)

print("\nImprimimos los datos")
lista.imprimir()

print("\nTamaño Lista")
print(lista.tamano())

print("\nBuscar")
print("1 esta en la lista:", lista.buscar(1))
print("2 esta en la lista:", lista.buscar(2))
print("3 esta en la lista:", lista.buscar(3))
print("4 esta en la lista:", lista.buscar(4))

lista.ordenar()
lista.imprimir()