# Grafos

Los grafos son una estructura de datos no lineal que se utiliza para representar relaciones entre objetos. Un grafo consiste en un conjunto de nodos (también conocidos como vértices) y un conjunto de aristas que conectan los nodos.

Cada nodo representa un objeto y cada arista representa una relación entre los objetos. Las aristas pueden tener un peso o una dirección, lo que significa que la relación entre dos objetos puede ser ponderada o unidireccional.

Los grafos se utilizan en muchos campos, incluyendo la informática, las matemáticas, la física, la biología y las redes sociales. Algunos ejemplos de aplicaciones de grafos incluyen el análisis de redes sociales, la optimización de rutas de transporte, la planificación de proyectos y la detección de fraudes en sistemas financieros.

Hay varios tipos de grafos, incluyendo grafos dirigidos, grafos no dirigidos, grafos ponderados y grafos bipartitos. Cada tipo tiene características únicas que lo hacen adecuado para diferentes tipos de problemas.

Los grafos se pueden representar de varias formas, como una matriz de adyacencia, una lista de adyacencia o una representación visual con nodos y aristas. La elección de la representación depende del problema específico que se esté resolviendo y de la eficiencia requerida en el procesamiento y almacenamiento de los datos.

En resumen, los grafos son una estructura de datos poderosa y flexible que se utiliza para representar relaciones entre objetos. Los grafos son aplicables a una amplia gama de problemas y se pueden representar de diferentes maneras para adaptarse a las necesidades específicas del problema.

## Problema del agente viajero

Formalmente, el TSP se puede definir como sigue: dado un conjunto de n ciudades, una matriz de distancias d_ij que indica la distancia entre cada par de ciudades i y j, y un punto de partida, encuentre la ruta más corta que visite cada ciudad exactamente una vez y regrese al punto de partida. El objetivo es minimizar la distancia total recorrida por el agente.

El TSP es conocido por ser un problema NP-duro, lo que significa que no hay un algoritmo eficiente conocido que pueda resolver el problema para cualquier número de ciudades en tiempo polinómico. Sin embargo, hay muchos algoritmos heurísticos y metaheurísticos que se pueden utilizar para resolver el TSP de manera aproximada, incluyendo:

Algoritmo del vecino más cercano: Este algoritmo comienza en una ciudad aleatoria y luego visita la ciudad más cercana hasta que se hayan visitado todas las ciudades. Luego, regresa al punto de partida. El algoritmo del vecino más cercano no garantiza encontrar la solución óptima, pero es rápido y a menudo produce soluciones aceptables.

Algoritmo 2-opt: Este algoritmo mejora iterativamente una solución inicial intercambiando pares de aristas en la ruta para reducir la distancia total recorrida. El algoritmo 2-opt no garantiza encontrar la solución óptima, pero puede mejorar significativamente las soluciones iniciales.

Algoritmos de búsqueda tabú: Estos algoritmos utilizan una lista tabú para evitar soluciones repetidas y explorar nuevas soluciones en el espacio de búsqueda. Los algoritmos de búsqueda tabú pueden ser muy efectivos para resolver el TSP, pero pueden requerir un tiempo de ejecución más largo.

Algoritmos genéticos: Estos algoritmos imitan el proceso de evolución biológica para encontrar soluciones óptimas. Los algoritmos genéticos son muy efectivos para resolver problemas combinatorios como el TSP, pero pueden requerir un tiempo de ejecución largo y muchas iteraciones para encontrar la solución óptima.

En resumen, el TSP es un problema clásico de optimización combinatoria que consiste en encontrar la ruta más corta que un agente puede tomar para visitar un conjunto de ciudades y regresar al punto de partida. Aunque el problema es NP-duro, hay muchos algoritmos heurísticos y metaheurísticos que se pueden utilizar para resolver el TSP de manera aproximada. En Python, puedes utilizar la librería NetworkX y la librería Pyomo para modelar y resolver el TSP como un problema de programación lineal entera (MILP).

> **BIbliotecas a usar**
>
> - [networkx](https://networkx.org/documentation/stable/index.html)
>
>- [Pyomo](http://www.pyomo.org/)

## Proyecto final

- Se hara uso grafos ponderados
- Se usara el algoritmo de Dijkstra

> Opciones:
>
> - Problema del viajero
> - Ruta mas optima
> - Redes sociales
> - Deteccion de fraudes

Con la libreria `pyomo` validamos el resultado de nuestro algoritmo
