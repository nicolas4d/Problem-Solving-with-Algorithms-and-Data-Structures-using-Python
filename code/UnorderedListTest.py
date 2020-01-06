import unittest
from UnorderedList import *

class TestNode(unittest.TestCase):
    def test_init(self):
        node = Node("node")

    def test_getData(self):
        node = Node("node")
        self.assertEqual(node.getData(), "node")

    def test_getNext(self):
        node = Node("node")
        self.assertEqual(node.getNext(), None)

    def test_setData(self):
        node = Node("node")
        node.setData("new data")
        self.assertEqual(node.getData(), "new data")

    def test_setNext(self):
        node = Node("node")
        node.setNext("next")
        self.assertEqual(node.getNext(), "next")

class TestUnorderedList(unittest.TestCase):
    def test_init(self):
        ulist = UnorderedList()

    def test_isEmpty(self):
        ulist = UnorderedList()
        self.assertEqual(ulist.isEmpty(), True)

    def test_add(self):
        ulist = UnorderedList()
        ulist.add(1)
        self.assertEqual(ulist.isEmpty(), False)
        self.assertEqual(ulist.head.getNext(), None)

    def test_size(self):
        ulist = UnorderedList()
        ulist.add(1)
        self.assertEqual(ulist.size(), 1)

    def test_search(self):
        ulist = UnorderedList()
        ulist.add(1)
        self.assertEqual(ulist.head.data, 1)
        self.assertEqual(ulist.head.next, None)
        self.assertEqual(ulist.search(1), True)

    def test_remove(self):
        ulist = UnorderedList()
        ulist.add(1)
        ulist.remove(1)
        self.assertEqual(ulist.isEmpty(), True)

    def test_append(self):
        ulist = UnorderedList()
        ulist.append(1)
        self.assertEqual(ulist.head.data, 1)
        ulist.append(2)
        self.assertEqual(ulist.head.next.data, 2)
        ulist.append(3)
        self.assertEqual(ulist.head.next.next.data, 3)
        
    def test_insert(self):
        ulist = UnorderedList()
        ulist.insert(0, 0)
        self.assertEqual(ulist.head.data, 0)
        self.assertEqual(ulist.head.getNext(), None)
        ulist.insert(1, 1)
        # self.assertEqual(ulist.head.getNext(), None)
        self.assertEqual(ulist.head.getNext().data, 1)

    def test_index(self):
        ulist = UnorderedList()
        ulist.append(0)
        self.assertEqual(ulist.index(0), 0)
        ulist.append(1)
        self.assertEqual(ulist.index(1), 1)

    def test_pop(self):
        ulist = UnorderedList()
        ulist.append(0)
        ulist.append(1)
        ulist.append(2)
        self.assertEqual(ulist.pop(2), 2)


if __name__ == '__main__':
    unittest.main()
