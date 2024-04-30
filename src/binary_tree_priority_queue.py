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
        self.root = self._insert_recursive(self.root, value, priority)

    def _insert_recursive(self, current, value, priority):
        if current is None:
            return Node(value, priority)
        elif priority <= current.priority:
            current.left = self._insert_recursive(current.left, value, priority)
            return current
        else:
            new_node = Node(value, priority)
            new_node.left = current
            return new_node

    def removal_with_hight_priority(self):
        if self.root:
            value = self.root.value
            self.root = self.root.left
            return value
        else:
            return None

    def hight_priority(self):
        if self.root:
            return self.root.value
        else:
            return None

    def display_queue(self):
        current = self.root
        while current:
            print(f"Value: {current.value}, Priority: {current.priority}")
            current = current.left
