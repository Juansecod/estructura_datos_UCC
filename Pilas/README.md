# Pilas

Una pila (también conocida como stack en inglés) es una estructura de datos lineal que se utiliza para almacenar elementos en una secuencia específica.

La pila se caracteriza por ser una estructura de datos de tipo LIFO (Last In, First Out), lo que significa que el último elemento que se agrega a la pila es el primero que se retira.

Las pilas tienen 3 operaciones básicas:

1. ***Push:*** esta operación permite agregar un elemento a la parte superior de la pila.
2. ***Pop:*** esta operación permite eliminar el elemento superior de la pila.
3. ***Peek:*** esta operación permite obtener el elemento superior de la pila sin eliminarlo.

Además, las pilas también pueden tener un tamaño máximo predefinido o ser dinámicas, lo que significa que su tamaño puede crecer o disminuir según se agregan o eliminan elementos.

Las pilas se utilizan en muchos ámbitos de la programación, como en la gestión de llamadas a funciones, en la implementación de algoritmos de búsqueda y en la evaluación de expresiones matemáticas, entre otros.

Se diferencia de las listas enlazadas ya que cuenta con los metodos apilar y desapilar, siendo push y pop respectivamente.

## Ejercicio
- Realizar un editor de texto por terminal. 
- Con base a esta informacion, debes crear un historial para el editor de texto. 
- Este tendra una capacidad configurable. 
- Cada vez que se haga la combinacion de teclas ```ctrl + z``` se devuelva