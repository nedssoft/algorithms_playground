
const DoublyLinkedList = class {
    constructor() {
        this.head = null;
        this.tail = null;
    }

    insertNode(nodeData) {
        let node = new DoublyLinkedListNode(nodeData);

        if (this.head == null) {
            this.head = node;
        } else {
            this.tail.next = node;
            node.prev = this.tail;
        }

        this.tail = node;
    }
};

function printDoublyLinkedList(node, sep, ws) {
    while (node != null) {
        ws.write(String(node.data));

        node = node.next;

        if (node != null) {
            ws.write(sep);
        }
    }
}

function sortedInsert(head, data) {
    // create our doubly linked list node 
    const newNode = new DoublyLinkedListNode();
    newNode.data = data;
​
    // base case 1: our current linked list node is null
    if (head === null) {
        // just return our newNode 
        return newNode;
​
    // base case 2: data <= our current linked list node's data
    } else if (data <= head.data) {
        newNode.next = head;
        head.prev = newNode;
        // return our newNode in this case since 
        // it's the new head of our linked list 
        return newNode;
    } else {
        // recursively call this function on the next node
        // of our linked list 
        // this will continue to re-curse until we find 
        // the spot where the data belongs 
        const rest = sortedInsert(head.next, data);
        // connect rest with our head 
        head.next = rest;
        rest.prev = head;
        // and we're done!
        // return our head node 
        return head;
    }
}