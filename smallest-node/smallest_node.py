
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
        else:
            self.insert_node(self.root, new_node)

    def insert_node(self, current_node, new_node):
        if new_node.value <= current_node.value:
            if current_node.left:
                self.insert_node(current_node.left, new_node)
            else:
                current_node.left = new_node
        elif new_node.value > current_node.value:
            if current_node.right:
                self.insert_node(current_node.right, new_node)
            else:
                current_node.right = new_node

    # find_smallest goes here
    def find_smallest(self):
        # If self.root does not exist, return None
        if self.root == None:
            return None
        # If self.root exists and there is no left, return value of root
        elif self.root and self.root.left == None:
            return self.root.value
        # Else, root.left does exist, so set root equal to root.left and recursively call function
        else:
            self.root = self.root.left
            return self.find_smallest()