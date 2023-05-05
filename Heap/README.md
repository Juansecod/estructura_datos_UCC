# Heap

Heap se encarga de distribuir todos los datos en un arbol binario. El metodo de llenado del arbol es distinto a como se trabaja normalmente. Para el llenado se nombra a cada uno de los nodos con un indice.

Es muy util para encotrar rutas, y es el mejor algoritmo para el ordenamiento.

Heap superior: Se ordena los elementos de arriba hacia abajo. El elemento mayor va estar en la primera posicion, osea el indice 0. Se van comparando los datos que ingresan y se intercambian recursivamente los numeros mayores. Para eliminar buscamos toda la referencia y seleccionamos el inferior para intercambiarlo con el primer nodo, y luego recursivamente organizar los nodos

Ejemplo:
Input -> 30, 12, 8, 90, 37, 50

Output ->               90
                    /       \
                   37       50
                 /   \     /  \
                12   30   8

Heap inferior: Se ordenan los elementos de arriba hacia abajo. El elemento menor va estar en la primera posicion, osea el indice 0. Se van comparando los datos que ingresan y se intercambian recursivamente los numeros menores.
