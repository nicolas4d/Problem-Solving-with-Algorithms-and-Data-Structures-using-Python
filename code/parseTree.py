from pythonds.basic import Stack
from pythonds.trees import BinaryTree

def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()            # following parent node
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for i in fplist:
        if i == '(' :
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()

        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()

        elif i == ')':
            currentTree = pStack.pop()

        elif i not in ['+', '-', '*', '/', ')']:  # operands
            try:
                currentTree.setRootVal(int(i))
                parent = pStack.pop()
                currentTree = parent

            except ValueError:
                raise ValueError("Token '{}' is not a valid integer.".format(i))

    return eTree

pt = buildParseTree("( ( 10 + 5 ) * 3 )")
pt.postorder()

'''
10
5
+
3
*
'''

print()

pt = buildParseTree("( ( 4 + 8 ) / ( 6 - 3 ) )")
pt.postorder()
"""
4
8
+
6
3
-
/
"""


import operator

def evaluate(parseTree):
    opers = {'+' : operator.add,
             '-' : operator.sub,
             '*' : operator.mul,
             '/' : operator.truediv}

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC :
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))  # here is recursion
    else :
        return parseTree.getRootVal()

print()
print(evaluate(pt))

'''
45
'''
