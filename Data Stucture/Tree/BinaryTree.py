class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

class BinaryTree:

    def __init__(self, rootData):
        self.root = Node(rootData)

    #root --> left --> right
    def preorderTravers(self, root):
        if not root:
            return
        print(root.data, end='==>')
        self.preorderTravers(root.leftChild)
        self.preorderTravers(root.rightChild)

    #left --> root --> right
    def inorderTravers(self, root):
        if not root:
            return
        self.inorderTravers(root.leftChild)
        print(root.data, end='==>')
        self.inorderTravers(root.rightChild)
        
    #left --> right --> root
    def postorderTravers(self, root):
        if not root:
            return
        self.postorderTravers(root.leftChild)
        self.postorderTravers(root.rightChild)
        print(root.data, end='==>')

tree = BinaryTree(8)
tree.root.leftChild = Node(3)
tree.root.rightChild = Node(10)
tree.root.leftChild.leftChild = Node(1)
tree.root.leftChild.rightChild = Node(6)
tree.root.leftChild.rightChild.leftChild = Node(4)
tree.root.leftChild.rightChild.rightChild = Node(7)
# tree.root.rightChild.leftChild = Node(6)
tree.root.rightChild.rightChild = Node(14)
tree.root.rightChild.leftChild = Node(13)


tree.preorderTravers(tree.root)
# tree.postorderTravers(tree.root)
# tree.inorderTravers(tree.root)

