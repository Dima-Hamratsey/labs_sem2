class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def find_successor(root: BinaryTree, node: BinaryTree) -> BinaryTree:
    def in_order_successor(current_node: BinaryTree, root: BinaryTree) -> BinaryTree:
        if not current_node:
            return None

        if current_node.right:
            return find_leftmost(current_node.right)

        successor = None
        while root:
            if current_node.value < root.value:
                successor = root
                root = root.left
            elif current_node.value > root.value:
                root = root.right
            else:
                break
        return successor

    def find_leftmost(node: BinaryTree) -> BinaryTree:
        while node.left:
            node = node.left
        return node

    if not node.parent or node.parent.right == node:
        return in_order_successor(node, root)

    return node.parent


root = BinaryTree(10)
root.left = BinaryTree(5)
root.right = BinaryTree(15)
root.left.left = BinaryTree(3)
root.left.right = BinaryTree(7)
root.right.right = BinaryTree(20)
root.right.right.left = BinaryTree(12)

node_7 = root.left.right
successor_node = find_successor(root, node_7)
if successor_node:
    print( successor_node.value)
