import unittest
from msdie import *

class TestMSDie(unittest.TestCase):
    def test_init(self):
        die = MSDie(4)

    def test_roll(self):
        print("teset_roll: ")

        die = MSDie(4)
        print(die.current_value)

    def test_str(self):
        print("test_str:")

        die = MSDie(4)
        for i in range(4):
            print(die)
            die.roll()

    def test_repr(self):
        print("test_repr")

        dieList = [MSDie(6), MSDie(7)]
        print(dieList)

if __name__ == '__main__':
    unittest.main()
