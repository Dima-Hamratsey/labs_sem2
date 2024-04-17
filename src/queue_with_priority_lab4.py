class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None

class PriorityQueue:
    def __init__(self):
        self.root = None

    def insert(self, value, priority):
        self.root = self.recursive(self.root, value, priority)

    def _insert_recursive_(self, current, value, priority):
        if current is None:
            return Node(value, priority)
        elif priority <= current.priority:
            current.left = self.recursive(current.left, value, priority)
            return current
        else:
            new_node = Node(value, priority)
            new_node.left = current
            return new_node

    def removal__highest_priority(self):
        if self.root:
            value = self.root.value
            self.root = self.root.left
            return value
        else:
            return None

    def highest_priority(self):
        if self.root:
            return self.root.value
        else:
            return None

    def display_queue(self):
        current = self.root
        while current:
            print(f"Value: {current.value}, Priority: {current.priority}")
            current = current.left
