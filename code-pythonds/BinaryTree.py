class BinaryTree:
    """
    A recursive implementation of Binary Tree
    Using links and Nodes approach.

    Modified to allow for trees to be constructed from other trees rather than always creating
    a new tree in the insertLeft or insertRight
    """

    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if isinstance(newNode, BinaryTree) :
            t = newNode
        else :
            t = BinaryTree(newNode)

        if self.leftChild is not None :
            t.left = self.leftChild

        self.leftChild = t

    def insertRight(self, newNode):
        if isinstance(newNode, BinaryTree) :
            t = newNode
        else :
            t = BinaryTree(newNode)

        if self.rightChild is not None :
            t.right = self.rightChild

        self.rightChild = t

    def isLeaf(self):
        return ((not self.leftChild) and (not self.rightChild))

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def inorder(self):
        if self.leftChild :
            self.leftChild.inorder()

        print(self.key)

        if self.rightChild :
            self.rightChild.inorder()

    def postorder(self):
        if self.leftChild :
            self.leftChild.postorder()

        if  self.rightChild:
            self.rightChild.postorder()

        print(self.key)

    def preorder(self):
        print(self.key)

        if self.leftChild :
            self.leftChild.preorder()

        if self.rightChild :
            self.rightChild.preorder()

    def printep(self):
        if self.leftChild :
            print('(', end=' ')
            self.leftChild.printep()

        print(self.key, end=' ')

        if self.rightChild :
            self.rightChild.printep()
            print(')', end=' ')

    def postordereval(self):
        opers = {'+' : operator.add,
                 '-' : operator.sub,
                 '*' : operator.mul,
                 '/' : operator.truediv}

        res1 = None
        res2 = None

        if self.leftChild :
            res1 = self.leftChild.postordereval()
        if self.rightChild :
            res2 = self.rightChild.postordereval()
        if res1 and res2 :
            return opers[self.key](res1, res2)
        else :
            return self.key


