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
        self.bond = []
        
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
                        self.bond.append(str(parent.value) + '->' + str(new.value))
                        self.size += 1
                        return
                else:
                    actual = actual.right
                    if actual == None:
                        parent.right = new
                        self.bond.append(str(parent.value) + '->' + str(new.value))
                        self.size += 1
                        return
    
    def search(self, value):
        actual = self.root
        while actual.value != value:
            if value < actual.value:
                actual = actual.left
                if actual == None:
                    return None
            else:
                actual = actual.right
                if actual == None:
                    return None
        return actual

    def pre_order_crossing(self, node):
        if node != None:
            print(node.value)
            self.pre_order_crossing(node.left)
            self.pre_order_crossing(node.right)

if __name__ == "__main__":                


    BT = BinaryTreeSearch()
    BT.insert(53)
    BT.insert(30)
    BT.insert(14)
    BT.insert(39)
    BT.insert(9)
    BT.insert(23)
    BT.insert(34)
    BT.insert(49)
    BT.insert(72)
    BT.insert(61)
    BT.insert(84)
    BT.insert(79)
    BT.insert(89)
    print(BT.root.value)
    print(BT.root.left.value)
    print(BT.root.right.value)
    print(BT.__len__())
    print(BT.bond)
    print(BT.search(10))
    print(BT.search(84))
    print(BT.search(100))
    print("--------------------------------")
    BT.pre_order_crossing(BT.root)