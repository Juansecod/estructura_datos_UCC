# Recursión

La recursividad es un concepto utilizado en programación y matemáticas que se refiere a la capacidad de una función o procedimiento para llamarse a sí mismo dentro de su propia definición. En otras palabras, una función recursiva es aquella que se define en términos de sí misma, y se utiliza para resolver problemas que se pueden dividir en subproblemas más pequeños y similares al problema original.

En términos más simples, la recursividad implica la solución de un problema dividiéndolo en problemas más pequeños, y luego resolviendo cada uno de ellos utilizando la misma función. Este proceso continúa hasta que se llega a un caso base, que es una solución trivial que no requiere recursión. Luego, la solución para cada subproblema se combina para obtener la solución final del problema original.

```py

""" Funcion recursiva que suma los numeros desde 0 hasta n """
def sumatoria(n):
    # Caso Base
    if n == 0
        return 0
    return n + sumatoria(n-1) # Se llama a si misma

```
