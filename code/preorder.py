def preorder(tree):
    if tree :
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

def preorder(self):
    print(self.key)

    if self.leftChild :
        self.leftChild.preorder()
    if self.rightChild :
        self.rightChild.preorder()
