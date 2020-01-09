import unittest
from hashTable import *

class TestHashTable(unittest.TestCase):
    def test_init(self):
        ht = HashTable()

    def test_put(self):
        ht = HashTable()
        ht.put(1, 1)
        self.assertEqual(ht.data[1], 1)
        ht.put(1, 2)
        self.assertEqual(ht.data[1], 2)
        ht.put(12, 2)
        self.assertEqual(ht.data[2], 2)
        ht.put(12, 3)
        self.assertEqual(ht.data[2], 3)

    def test_hashfunction(self):
        ht = HashTable()
        self.assertEqual(ht.hashfunction(3, 11), 3)

    def test_rehash(self):
        ht = HashTable()
        self.assertEqual(ht.rehash(3, 11), 4)

    def test_get(self):
        ht = HashTable()
        ht.put(1, 1)
        self.assertEqual(ht.get(1), 1)

    def test_comprehensive(self):
        H=HashTable()
        H[54]="cat"
        H[26]="dog"
        H[93]="lion"
        H[17]="tiger"
        H[77]="bird"
        H[31]="cow"
        H[44]="goat"
        H[55]="pig"
        H[20]="chicken"
        print(H.slots)
        print(H.data)

        print(H[20])

        print(H[17])
        H[20]='duck'
        print(H[20])
        print(H[99])

if __name__ == '__main__':
    unittest.main()
