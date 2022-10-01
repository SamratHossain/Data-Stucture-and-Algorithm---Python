class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

class BinarySearchTree:

    def __init__(self, rootData):
        self.root = Node(rootData)

    def FindElement(self, root, data):

        currentNode = root

        while currentNode:
            if data == currentNode.data:
                return print(currentNode.data)
            elif data < currentNode.data:
                currentNode = currentNode.leftChild
            else:
                currentNode = currentNode.rightChild
        return print("Node Not Exist")

    def FindMin(self, root):
        currentNode = root
        if currentNode == None:
            return None
        while currentNode.leftChild != None:
            currentNode = currentNode.leftChild
        return print(f"Minimum Value is: {currentNode.data}")

    def FindMax(self, root):
        currentNode = root
        if currentNode == None:
            return None
        while currentNode.rightChild != None:
            currentNode = currentNode.rightChild
        return print(f"Max Value is: {currentNode.data}")

    def InsertNode(self, root, node):
        if root == None:
            root = node
        else:
            if node.data < root.data:
                if root.leftChild == None:
                    root.leftChild = node
                    print(f"Insert Node Successfully LeftChild {node.data}")
                else:
                    self.InsertNode(root.leftChild, node)
                    
            else:
                if root.rightChild == None:
                    root.rightChild = node
                    print(f"Insert Node Successfully RightChild {node.data}")
                else:
                    self.InsertNode(root.rightChild, node)
                    

    

    

tree = BinarySearchTree(8)
tree.root.leftChild = Node(3)
tree.root.rightChild = Node(10)
tree.root.leftChild.leftChild = Node(1)
tree.root.leftChild.rightChild = Node(6)
tree.root.leftChild.rightChild.leftChild = Node(4)
tree.root.leftChild.rightChild.rightChild = Node(7)
# tree.root.rightChild.leftChild = Node(6)
tree.root.rightChild.rightChild = Node(14)
tree.root.rightChild.rightChild.leftChild = Node(13)

# tree.FindElement(tree.root, 13)
# tree.FindMin(tree.root)
node = Node(17)
tree.InsertNode(tree.root, node)
tree.FindMax(tree.root)





