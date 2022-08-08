class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def print_value(self):
        print(self.value)

class BinaryTreeSearch:
    def __init__(self):
        self.root = None
        self.size = 0
    def __len__(self):
        return self.size
