# Programación Orientada a Objetos (POO)

- [¿Que es POO?](README.md#¿que-es-la-poo)
- [Ejercicios](README.md#ejercicio-1)

## ¿Que es la POO?

La Programación Orientada a Objetos es un paradigma de la programación el cual busca llevar el mundo real a una representación mediante objetos, en donde una clase es por decirlo de algun modo un modelo de la caracteristicas que tiene un objeto. Un objeto ya es una instancia de esta clase en la cual le asignamos unos atributos y podremos ejecutar los metodos definidos.

### Clase

Como lo mencionaba anteriormente, una clase es un modelo, una representacion de algo del mundo real llevado a un objeto que cuenta con unos `atributos` y unos `metodos`.

Comunmente la estructura de una clase en la mayoria de lenguajes de programacion es la siguiente:

```js
    class NombreClase extends ClasePadre{
        atributos;
        constructor(){
            //Inicializa el objeto asignandole los atributos ya sea con valores por defecto o asignado por el usuario
        }

        metodos(){
            //Los metodos son las funciones que tiene el objeto, que se representan como acciones que tiene este objeto en el mundo real, como por ejemplo caminar para una persona
        }
    }
```

### Atributos y Metodos

Los atributos y metodos en la programación vienen a ser las caractiristicas y las acciones respectivamente que tiene.

```js
    //Consulto el valor de un atributo publico
    nombreObjeto.atributo;
    //Ejecuto un metodo del objeto
    nombreObjeto.metodo();
```

Ambos cuentan con 3 diferentes tipos, los publicos, los privados y los protegidos. Los publicos son aquellos que se tienen acceso en cualquier parte del codigo. Los privados son aquellos que solo se pueden llamar dentro de la propia clase. Los protegidos son similares a los privados, con la unica diferencia que los protegidos si se pueden acceder dentro de las clases hijas.

```js
    //Normalmente se declaran de la siguiente manera
    Publico;
    _Privado;
    __Protegido;
```

### Objetos

Los objetos son instancias de las clases, en donde ya podremos hacer uso de sus atributos y metodos publicos.

Normalmente se instancian las clases de la siguiente forma:

```js
    const nombreObjeto = new NombreClase();
```

>***Nota:*** La programacion Orientada a Objetos cuenta con 4 caracteristicas: Herencia, encapsulamiento, polimorfismo y abstraccion.

## **Ejercicio 1**

Crear una clase llamada Vehículo, esta clase debe recibir 2 parámetros, marca y combustible; la clase también debe contener dos métodos encender y arrancar.

Instanciar la clase y usar el método mágico ```__str__``` para imprimir la marca y el combustible usado.

- [Solución (Python)](https://replit.com/@DiegoArcila/Clases#main.py)
- [Solución (Dart)](https://replit.com/@DiegoArcila/DartED#main.dart)
- [Solución (PHP)](https://replit.com/@DiegoArcila/phpED#Clases/Ejercicio1.php)
- [Solución (Node)](https://replit.com/@DiegoArcila/NodeED#Clases/Ejercicio1.js)

## **Ejercicio 2**

Crear dos clases, Moto y Carro, estas clases deben estar heradadas de la clase Vehiculo.

Realizar dos instancias de las nuevas clases creadas e imprimir el objeto instanciado.

- [Solución (Python)](https://replit.com/@DiegoArcila/Clases#ejercicio2.py)
- [Solución (Dart)](https://replit.com/@DiegoArcila/DartED#ejercicio2.dart)
- [Solución (PHP)](https://replit.com/@DiegoArcila/phpED#Clases/Ejercicio2.php)
- [Solución (Node)](https://replit.com/@DiegoArcila/NodeED#Clases/Ejercicio2.js)

## **Ejercicio 3**

La clase Vehiculo, debe tener una propiedad llamada tipo (esta contendrá el tipo de vehiculo - Carro o Moto -), esta propiedad debe ser seteada al momento de instanciar la clase Carro o Moto y al momento de imprimir el objeto debe indicar el tipo de vehiculo junto con el texto mostrado anteriormente.

- [Solución (Python)](https://replit.com/@DiegoArcila/Clases#ejercicio3.py)
- [Solución (Dart)](https://replit.com/@DiegoArcila/DartED#ejercicio3.dart)
- [Solución (PHP)](https://replit.com/@DiegoArcila/phpED#Clases/Ejercicio3.php)
- [Solución (Node)](https://replit.com/@DiegoArcila/NodeED#Clases/Ejercicio3.js)

## **Ejercicio 4**

Hacer control de encendido de los vehiculos, para esto al momento de usar el método encender, se debe validar el nivel de combustible del vehiculo (medida dada en galones) no este por debajo de un 10%, si este tiene un nivel muy bajo, mostrar la advertencia que necesita ir a la gasolinera.

- [Solución (Python)](https://replit.com/@DiegoArcila/Clases#ejercicio4.py)
- [Solución (Dart)](https://replit.com/@DiegoArcila/DartED#ejercicio4.dart)
- [Solución (PHP)](https://replit.com/@DiegoArcila/phpED#Clases/Ejercicio4.php)
- [Solución (Node)](https://replit.com/@DiegoArcila/NodeED#Clases/Ejercicio4.js)

## **Ejercicio 5**

Debes hacer un ejercicio donde por medio de un método, el vehículo de marcha y haga un consumo de combustible a medida que este funcione, cuando llegue a los niveles de combustible definidos en el mensaje anterior, muestre la advertencia y si esta llega a cero, detenga la marcha.

- [Solución (Python)](https://github.com/Juansecod/estructura_datos_UCC/blob/main/POO/Vehiculo.py)
- [Solución (Dart)](https://github.com/Juansecod/estructura_datos_UCC/blob/main/POO/Vehiculo.dart)
- [Solución (PHP)](https://github.com/Juansecod/estructura_datos_UCC/blob/main/POO/Vehiculo.php)
- [Solución (Node)](https://github.com/Juansecod/estructura_datos_UCC/blob/main/POO/Vehiculo.js)
