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
        if (this.is_empty()) return undefined;
        const poppedNode = this.head
        this.head = this.head.next;
        poppedNode.next = undefined;
        return poppedNode;
    }

    peek(){
        
    }
}