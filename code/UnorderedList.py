class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0

        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False

        while current != None and not found:
            if current.getData() == item :
                found = True
            else :
                current = current.getNext

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = None

        while not found:
            if current.getData() == item :
                found = True
            else :
                previous = current
                current = current.getNext()

        if found :
            if previous == None :
                self.head = current.getNext()
            else :
                previous.setNext(current.getNext())

    def append(self, item):
        current = self.head
        previous = None

        while current != None:
            previous = current
            current = current.getNext()

        if previous == None :
            self.head = Node(item)
        else :
            node = Node(item)
            previous.next = node

    def insert(self, index, item):
        assert index <= self.size(), "out of range."

        if self.head is None :
            self.head = Node(item)
        else :
            current = self.head

            for i in range(index - 1):
                current = current.getNext()

            node = Node(item)
            node.setNext(current.getNext())
            current.setNext(node)

    def index(self, index):
        assert index < self.size(), "out of range."

        current = self.head

        for i in range(index):
            current = current.getNext()

        return current.data

    def pop(self, index = 0):
        assert index < self.size(), "out of range."

        current = self.head
        previous = None

        for i in range(index):
            previous = current
            current = current.getNext()

        print(current.data)

        if previous is None :
            self.head = current.getNext()
            return current.getData()
        else :
            previous.setNext(current.getNext())
            return current.getData()
