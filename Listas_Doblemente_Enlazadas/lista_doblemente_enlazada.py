class Nodo:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
    
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
            
    def mostrar(self):
        if self.es_vacio():
            return
        nodo = self.cabeza
        while nodo.next != None:
            print(nodo.data, end = ",")
            nodo = nodo.next
        print(nodo.data)

lista = ListaDoblementeEnlazada()

for i in range(1,6):
    lista.insertar(i)
    
lista.mostrar()            