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

    def insert(self, value):
        new = Node(value)
        if self.size == 0:
            self.root = new
            self.size += 1
        else:
            actual = self.root
            while True:
                parent = actual
                if value < actual.value:
                    actual = actual.left
                    if actual == None:
                        parent.left = new
                    return
                else:
                    actual = actual.right
                    if actual == None:
                        parent.right = new
                        return
        self.size += 1

