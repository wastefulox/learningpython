# We'll be using our Node class
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node


# Create your LinkedList class below:
class LinkedList:
    def __init__(self, value=None):
        self.value = value
        self.head_node = Node(self.value)

    def get_head_node(self):
        return self.head_node

ll = LinkedList(19)
print(ll.get_head_node().value)