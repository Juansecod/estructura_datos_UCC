""" Instrucciones
-Crear una clase animal con los métodos y atributos básicos. en uno de los atributos, debes indicar la edad y el tipo de animal (Águila, pantera, vaca, ...)
-Crear una lista enlazada que permita agregar animales al listado, donde al momento de agregar un nuevo animal a la lista, esta no debe repetirse
-Para mostrar los animales que contiene la lista enlazada, debes realizarla usando dos métodos
    *Una función recursiva
    *Un bucle 
"""
import os

os.system("cls")


class Animal:
    # Atributos
    edad: int
    tipo: str
    
    def __init__(self, edad, tipo):
        self.edad, self.tipo = edad, tipo
        
    def __str__(self):
        return (f"Tipo: {self.tipo}, Edad: {self.edad}")
    
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.next = None
        
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        
    def es_vacio(self):
        return self.cabeza is None
    
    def buscar(self, dato):
        nodo = self.cabeza
        if nodo.dato == dato:
            return True
        while nodo is not None:
            if nodo.dato == dato:
                return True
            nodo = nodo.next
        return False
    
    def agregar(self, dato):
        nodo = Nodo(dato)
        if self.es_vacio():
            self.cabeza = nodo
        elif self.cabeza.dato.tipo == dato.tipo:
            return
        else:
            nodo_actual = self.cabeza
            es_nuevo = True
            while nodo_actual.next is not None:
                if nodo_actual.dato.tipo == dato.tipo:
                    es_nuevo = False
                nodo_actual = nodo_actual.next
            if es_nuevo:
                nodo_actual.next = nodo
                
    def str_bucle(self):
        if(self.es_vacio()):
            return
        nodo = self.cabeza
        lista = ""
        while nodo is not None:
            lista = lista + nodo.dato.__str__() + "\n"
            nodo = nodo.next
        return lista
            
    def str_recursivo(self, nodo = None):
        if(self.es_vacio()):
            return
        if nodo == None:
            nodo = self.cabeza
        if nodo.next == None:
            return nodo.dato.__str__()
        return nodo.dato.__str__() + "\n" + self.str_recursivo(nodo.next)
    
    def mostrar_bucle(self):
        if(self.es_vacio()):
            return
        nodo = self.cabeza
        lista = ""
        while nodo is not None:
            print(nodo.dato.__str__())
            nodo = nodo.next
            
    def mostrar_recursivo(self, nodo = None):
        if(self.es_vacio()):
            return
        if nodo == None:
            nodo = self.cabeza
        print(nodo.dato.__str__())
        if nodo.next == None:
            return
        self.mostrar_recursivo(nodo.next)
            
perro = Animal(10, "Perro")
perro2 = Animal(12, "Perro")
gato = Animal(4, "Gato")
aguila = Animal(4, "Aguila")
vaca = Animal(4, "Vaca")

lista_animales = ListaEnlazada()
lista_animales.agregar(perro)
lista_animales.agregar(perro2)
lista_animales.agregar(gato)
lista_animales.agregar(aguila)
lista_animales.agregar(vaca)

print("     Mostar con Bucle:")
lista_animales.mostrar_bucle()
print("-"*50)
print("     Mostar con Recursion:")
lista_animales.mostrar_recursivo()

print("\n\nString con bucle")
print(lista_animales.str_bucle())
print("-"*50)
print("String con recursividad")
print(lista_animales.str_recursivo())
