from pythonds.basic import Stack

def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()
    traceOpStack = []

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789" :
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
            traceOpStack.append(token)
            print(traceOpStack)
        elif token == ')':
            topToken = opStack.pop()
            traceOpStack.pop()
            print(traceOpStack)

            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()

                traceOpStack.pop()
                print(traceOpStack)

        else :
            while (not opStack.isEmpty()) and \
                  (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
                traceOpStack.pop()
                print(traceOpStack)

            opStack.push(token)
            traceOpStack.append(token)
            print(traceOpStack)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
        traceOpStack.pop()
        print(traceOpStack)

    return " ".join(postfixList)


print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))

'''
A B * C D * +
A B + C * D E - F G + * -
'''

print(infixToPostfix("( A + B ) * ( C + D )"))
'A B + C D + *'
print(infixToPostfix("( A + B ) * C"))
'A B + C *'
print(infixToPostfix("A + B * C"))
'A B C * +'

