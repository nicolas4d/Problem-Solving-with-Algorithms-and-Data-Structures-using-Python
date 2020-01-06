import unittest
from stack import *

class TestStack(unittest.TestCase):
    def test_init(self):
        s = Stack()

    def test_isEmpty(self):
        s = Stack()
        self.assertEqual(s.isEmpty(), True)

    def test_push(self):
        s = Stack()
        s.push(0)
        self.assertEqual(s.isEmpty(), False)

    def test_pop(self):
        s = Stack()
        s.push(0)
        self.assertEqual(s.pop(), 0)

    def test_peek(self):
        s = Stack()
        s.push(0)
        self.assertEqual(s.peek(), 0)
        self.assertEqual(s.pop(), 0)

    def test_size(self):
        s = Stack()
        s.push(0)
        self.assertEqual(s.size(), 1)


if __name__ == '__main__':
    unittest.main()
