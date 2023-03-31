class Nodo:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
class Lista:
    def __init__(self):
        self.cabeza = None
        self.ultimo = None
        self.actual = None
    
    def es_vacio(self):
        return self.cabeza is None
    
    def insertar(self, data):
        nuevo_nodo =  Nodo(data)
        if self.es_vacio():
            self.cabeza = nuevo_nodo
        else:
            ultimo_nodo = self.actual
            nuevo_nodo.prev = ultimo_nodo
            ultimo_nodo.next = nuevo_nodo
        
        self.ultimo = nuevo_nodo
        self.actual = nuevo_nodo
            
    def mostrar(self):
        if self.es_vacio():
            return
        nodo = self.cabeza
        while nodo.next != None:
            print(nodo.data, end = ",")
            nodo = nodo.next
        print(nodo.data)

    def previo(self):
        try:
            if self.actual.prev is None:
                raise Exception()
            
            self.actual = self.actual.prev
            return self.actual.data
            
        except Exception as e:
            return None
    
    def siguiente(self):
        try:
            if self.actual.next is None:
                raise Exception()
                
            self.actual = self.actual.next
            return self.actual.data
        except:
            return None
    