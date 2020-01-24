class LogicGate:
    def __init__(self, n):
        self.name = n
        self.output = None

    def getLabel(self):
        return self.name

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

    def performGateLogic(self):
        return "performGateLogic"

class BinaryGate(LogicGate):
    def __init__(self, n):
        super(BinaryGate, self).__init__(n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None :
            return int(input("Enter Pin A input for gate " + \
                              self.getLabel() + \
                              "-->"))
        else :
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None :
            return int(input("Enter Pin B input for gate " + \
                             self.getLabel() + \
                             "-->"))
        else :
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pinA == None :
            self.pinA = source
        else :
            if self.pinB == None :
                self.pinB = source
            else :
                print("Cannot connect: NO EMPTY PINS on this gate")

class AndGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 and b == 1 :
            return 1
        else :
            return 0

class OrGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 or b == 1 :
            return 1
        else :
            return 0

class UnaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pin = None

    def getPin(self):
        if self.pin == None :
            return int(input("Enter Pin input for gate " + \
                             self.getLabel() + \
                             "-->"))
        else :
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pin == None :
            self.pin = source
        else :
            print("Cannot Connect: NO EMPTY PINS on this gate")

class NotGate(UnaryGate):
    def __init__(self, n):
        UnaryGate.__init__(self, n)

    def performGateLogic(self):
        if self.getPin() :
            return 0
        else :
            return 1

class NandGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 and b == 1 :
            return 0
        else :
            return 1

class NorGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 or b == 1 :
            return 0
        else :
            return 1

class HalfAdder(BinaryGate):
    def __init__(self):
        "init"
        BinaryGate.__init__(self, "halfAdder")

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == b :
            return 0
        else :
            return 1

class Connector:
    def __init__(self, fgate, tgate):
        "init"
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate
