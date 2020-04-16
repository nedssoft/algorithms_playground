class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
    new_node = DoublyLinkedListNode(data)
    if not head:
        return new_node
    current = head
    if current.data > data:
        new_node.next = current
        current.prev = new_node
        return new_node
    while current.next:
        if data > current.data and data <= current.next.data:
            new_node.next = current.next
            current.next.prev = new_node
            current.next=new_node
            new_node.prev=current
            break
        else:
            current = current.next
    else:
        current.next=new_node
        new_node.prev=current
    return head