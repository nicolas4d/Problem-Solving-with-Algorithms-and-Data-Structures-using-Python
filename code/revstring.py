from pythonds.basic import Stack

def revstring(mystr):
    stack = Stack()

    for ch in mystr:
        stack.push(ch)

    newStr = ""
    while not stack.isEmpty():
        newStr += stack.pop()

    return newStr

assert revstring('apple') == 'elppa', ""
assert revstring('x') == 'x', ""
assert revstring('1234567890') == '0987654321' ,""
