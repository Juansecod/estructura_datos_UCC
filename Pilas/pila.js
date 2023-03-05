class Node{
    constructor(data){
        this.data = data;
        this.next = undefined;
    }
}

class Stack{
    constructor(){
        this.head = undefined;
    }

    isEmpty(){
        return this.head == undefined;
    }

    push(data){
        const newNode = new Node(data);
        newNode.next = this.head;
        this.head = newNode;
    }

    pop(){
        if (this.isEmpty()) return undefined;
        const poppedNode = this.head;
        this.head = this.head.next;
        poppedNode.next = undefined;
        return poppedNode;
    }

    peek(){
        if (this.isEmpty()) return undefined;
        return this.head.data;
    }

    display(){
        if (this.isEmpty()) return undefined;
        let current = this.head;
        while (current){
            console.log(current.data + '->');
            current = current.next;
        }
        return;
    }
}

const stack = new Stack();

/* Apilamos los datos dentro de la pila */
stack.push("Primer Elemento");
stack.push("Segundo Elemento");
stack.push("Tercero Elemento");
stack.push("Cuarto Elemento");

/* Mostramos el dato que esta en la cabeza */
console.log("Primer dato en salir:");
console.log(stack.peek());
console.log("-".repeat(50));

/* Mostramos todos los datos que hay dentro de la pila */
console.log("Elementos de la pila: ");
stack.display();
console.log("-".repeat(50));

/* Desapilamos dos elementos */
stack.pop();
stack.pop();

/* Mostramos la pila ahora con los elementos desapilados */
console.log("Elementos de la pila luedo de desapilarla dos veces: ");
stack.display();
console.log("-".repeat(50));