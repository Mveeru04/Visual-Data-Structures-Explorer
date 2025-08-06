class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        # Insert at end
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove(self):
        if self.head:
            self.head = self.head.next

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

linked_list = LinkedList()

def insert(value):
    linked_list.insert(value)
    return linked_list.to_list()

def remove():
    linked_list.remove()
    return linked_list.to_list()

def get():
    return linked_list.to_list()
