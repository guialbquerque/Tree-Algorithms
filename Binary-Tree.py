from webbrowser import get


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
    # root, left, right
    def pre_order_crossing(self, node):
        if node != None:
            print(node.value)
            self.pre_order_crossing(node.left)
            self.pre_order_crossing(node.right)

    #left, root, right
    def in_order_crossing(self, node):
        if node != None:
            self.in_order_crossing(node.left)
            print(node.value)
            self.in_order_crossing(node.right)

    #left, right, root
    def post_order_crossing(self, node):
        if node != None:
            self.post_order_crossing(node.left)
            self.post_order_crossing(node.right)
            print(node.value)

    def remove_node(self, value):
        if self.size == 0:
            print("The tree is empty!")
            return
        actual = self.root
        parent = self.root
        is_left = True

        #The initial search of the value
        while actual.value != value:
            parent =  actual
            if value < actual.value:
                is_left = True
                actual = actual.left
            else:
                is_left = False
                actual = actual.right
            if actual == None:
                return False
        #The node to be remove is a leaf node
        if actual.left == None and actual.right == None:
            if actual == self.root:
                self.root = None
            elif is_left == True:
                self.bond.remove(str(parent.value) + '->' + str(parent.left.value))
                parent.left = None
            else:
                self.bond.remove(str(parent.value) + '->' + str(parent.right.value))
                parent.right = None

        #The node to be remove has a single child and is the right side of the tree
        elif actual.left == None:
            if is_left == True:

                self.bond.remove(str(parent.value) + '->' + str(actual.value))
                self.bond.remove(str(actual.value) + '->' + str(actual.right.value))

                parent.left = actual.right
                self.size -= 1
                self.bond.append(str(parent.value) + '->' + str(actual.right.value))
                
            else:

                self.bond.remove(str(parent.value) + '->' + str(actual.value))
                self.bond.remove(str(actual.value) + '->' + str(actual.right.value))
                parent.right = actual.right
                self.size -= 1
                self.bond.append(str(parent.value) + '->' + str(actual.right.value))

        #The node to be remove has a single child and is the left side of the tree
        else:

            if is_left == True:

                self.bond.remove(str(parent.value) + '->' + str(actual.value))
                self.bond.remove(str(actual.value) + '->' + str(actual.left.value))

                parent.left = actual.left
                self.size -= 1
                self.bond.append(str(parent.value) + '->' + str(actual.left.value))

            else:

                self.bond.remove(str(parent.value) + '->' + str(actual.value))
                self.bond.remove(str(actual.value) + '->' + str(actual.left.value))
                parent.right = actual.left
                self.size -= 1
                self.bond.append(str(parent.value) + '->' + str(actual.left.value))
    
    def get_Successor(self, node):
        parent_successor = node
        successor = node
        actual = node.right
        while actual != None:
            parent_successor = successor
            successor = actual
            actual = actual.left
        if successor != node.right:
            parent_successor.left = actual
            successor.right = node.right

        return successor
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
    print('--------------------------------')
    BT.in_order_crossing(BT.root)
    print('--------------------------------')
    BT.post_order_crossing(BT.root)
    print("--------------------------------")
    BT.remove_node(84)
    print(BT.bond)
    BT.remove_node(9)
    print('--------------------------')
    print(BT.bond)
    print(BT.remove_node(14))
    print('--------------------------')
    print(BT.bond)
    print(BT.size)
    print('-------------------------')
    print(BT.get_Successor(BT.root.right))