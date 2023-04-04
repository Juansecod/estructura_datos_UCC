class Nodo:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.ultimo = None
        
    def es_vacio(self):
        return self.cabeza is None
    
    def insertar(self, data):
        nuevo_nodo =  Nodo(data)
        if self.es_vacio():
            self.cabeza = nuevo_nodo
        else:
            ultimo_nodo = self.cabeza
            while ultimo_nodo.next != None:
                ultimo_nodo = ultimo_nodo.next
            nuevo_nodo.prev = ultimo_nodo
            ultimo_nodo.next = nuevo_nodo
        self.ultimo = nuevo_nodo
            
    def mostrar(self):
        if self.es_vacio():
            return
        nodo = self.cabeza
        while nodo.next != None:
            print(nodo.data, end = ",")
            nodo = nodo.next
        print(nodo.data)
        
    def delete(self, data):
      current_node = self.cabeza
      if current_node.data == data:
          self.cabeza = current_node.next
          self.cabeza.prev = None
          return
      elif self.ultimo.data == data:
          self.ultimo.prev.next = None
          return
          
      while current_node.next is not None:
          if current_node.next.data == data:
              current_node.next = current_node.next.next
              current_node.next.prev = current_node
              return
          current_node = current_node.next

lista = ListaDoblementeEnlazada()

for i in range(1,6):
    lista.insertar(i)
print("Antes de eliminar:")
lista.mostrar()

lista.delete(5)
print("\nLuego de eliminar:")    
lista.mostrar()            