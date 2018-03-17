class Node {
    constructor(value){
    this.val = value;
    this.next = null;
    }
}

class Slist {

    constructor(){
    this.head=null;}

    addFront(value){
        var n = new Node(value);
        n.next = this.head;
        this.head = n;
        return this;
    }

    removeFront(){
        if (!this.head){
            return this;
        }
        var temp = this.head;
        this.head = this.head.next;
        temp.next = null;
        return this;
    }

    front(){
        if (!this.head){
            return null;
        }
        return this.head.val;
    }
}

var list = new Slist();
list.addFront("A").addFront("B");
console.log(list.front());