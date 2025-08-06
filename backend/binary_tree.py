class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        # Use integer comparison for numeric ordering
        if int(value) < int(node.value):
            if node.left:
                self._insert_recursive(node.left, value)
            else:
                node.left = TreeNode(value)
        else:
            if node.right:
                self._insert_recursive(node.right, value)
            else:
                node.right = TreeNode(value)

    def remove(self):
        self.root = None

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)

    def get_inorder_list(self):
        result = []
        self._inorder(self.root, result)
        return result

binary_tree = BinaryTree()

def insert(value):
    binary_tree.insert(value)
    return get()

def remove():
    binary_tree.remove()
    return get()

def get():
    return binary_tree.get_inorder_list()
