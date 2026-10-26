class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def print_forward(self):
        current = self.head
        while current:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")

    def print_backward(self):
        current = self.tail
        while current:
            print(current.value, end=" <-> ")
            current = current.prev
        print("None")

    def find(self, value):
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def delete(self, value):
        node_to_delete = self.find(value)
        if not node_to_delete:
            return False
        if node_to_delete.prev:
            node_to_delete.prev.next = node_to_delete.next
        else:
            self.head = node_to_delete.next
        if node_to_delete.next:
            node_to_delete.next.prev = node_to_delete.prev
        else:
            self.tail = node_to_delete.prev
        return True

    def insert_after(self, target_value, new_value):
        target_node = self.find(target_value)
        if not target_node:
            return False
        new_node = Node(new_value)
        new_node.prev = target_node
        new_node.next = target_node.next
        if target_node.next:
            target_node.next.prev = new_node
        else:
            self.tail = new_node
        target_node.next = new_node
        return True