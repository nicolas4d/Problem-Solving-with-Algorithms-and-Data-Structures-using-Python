import unittest
from logicGate import *

class TestLogicGate(unittest.TestCase):
    def test_init(self):
        lg = LogicGate("name")
        self.assertEqual(lg.name, "name")
        self.assertEqual(lg.output, None)

    def test_getLabel(self):
        lg = LogicGate("name")
        self.assertEqual(lg.getLabel(), "name")

    def test_performGateLogic(self):
        lg = LogicGate("name")
        self.assertEqual(lg.performGateLogic(), "performGateLogic")

    def test_getOutput(self):
        lg = LogicGate("name")
        self.assertEqual(lg.getOutput(), "performGateLogic")

class TestBinaryGate(unittest.TestCase):
    def test_init(self):
        bg = BinaryGate("name")
        self.assertEqual(bg.name, "name")
        self.assertEqual(bg.output, None)
        self.assertEqual(bg.pinA, None)
        self.assertEqual(bg.pinB, None)

    def test_getPinA(self):
        bg = BinaryGate("BinaryGate")
        # print(bg.getPinA())

    def test_getPinB(self):
        bg = BinaryGate("BinaryGate")
        # print(bg.getPinB())

    def test_setNextPin(self):
        bg = BinaryGate("BinaryGate")
        bg.setNextPin("setNextPin")
        self.assertEqual(bg.pinA, "setNextPin")
        bg.setNextPin("pinB")
        self.assertEqual(bg.pinB, "pinB")

class TestAndGate(unittest.TestCase):
    def test_init(self):
        ag = AndGate("And Gate")

    def test_performGateLogic(self):
        ag = AndGate("And Gate")
        # self.assertEqual(ag.performGateLogic(), 1)

class TestOrGate(unittest.TestCase):
    def test_orgate(self):
        og = OrGate("Or Gate")
        # print(og.performGateLogic())


class TestUnaryGate(unittest.TestCase):
    def test_init(self):
        ug = UnaryGate("Unary Gate")

    def test_getPin(self):
        ug = UnaryGate("Unary Gate")
        # print(ug.getPin())

    def test_setNextPin(self):
        ug = UnaryGate("Unary Gate")

class TestNotGate(unittest.TestCase):
    def test_init(self):
        ng = NotGate("Not Gate")

    def test_performGateLogic(self):
        ng = NotGate("Not Gate")
        # print(ng.performGateLogic())

class TestNandGate(unittest.TestCase):
    def test_init(self):
        ng = NandGate("Nand Gate ")

    def test_performGateLogic(self):
        ng = NandGate("Nand Gate ")
        # print(ng.performGateLogic())

class TestNorGate(unittest.TestCase):
    def test_init(self):
        ng = NorGate("Nor Gate")

    def test_performGateLogic(self):
        ng = NorGate("Nor Gate")
        # print(ng.performGateLogic())

class TesthalfAdder(unittest.TestCase):
    def test_init(self):
        hf = HalfAdder()

    def test_performGateLogic(self):
        hf = HalfAdder()
        # print(hf.performGateLogic())

class TestConnector(unittest.TestCase):
    def test_init(self):
        andGate = AndGate("And Gate")
        orGate = OrGate("Or Gate")
        c = Connector(andGate, orGate)
        # orGate.getOutput()

class TestComprehensive(unittest.TestCase):
    def test_comprehensive(self):
        # g1 = AndGate("G1")
        # g2 = AndGate("G2")
        # g3 = OrGate("G3")
        # g4 = NotGate("G4")
        # c1 = Connector(g1,g3)
        # c2 = Connector(g2,g3)
        # c3 = Connector(g3,g4)
        # print(g4.getOutput())

        # print("NandGate: ")
        # nandGate = NandGate("nandGate")
        # print(nandGate.performGateLogic())

        # print("NorGate: ")
        # norGate = NorGate("NorGate")
        # print(norGate.performGateLogic())


        # g1 = AndGate("g1")
        # g2 = AndGate("g2")
        # g3 = NorGate("g3")
        # Connector(g1, g3)
        # Connector(g2, g3)
        # print(g3.getOutput())

        # g4 = NandGate("g4")
        # g5 = NandGate("g5")
        # g8 = AndGate("g8")
        # Connector(g4, g8)
        # Connector(g5, g8)
        # print(g8.getOutput())

        pass

if __name__ == '__main__':
    unittest.main()
