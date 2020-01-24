# greatest common divisor
def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn

    return n

class Fraction:
    def __init__(self, top, bottom):
        topInt = int(top)
        bottomInt = int(bottom)

        if bottomInt < 0 :
            topInt = - topInt

        common = gcd(topInt, bottomInt)
        self.num = topInt // common
        self.den = bottomInt // common

    def show(self):
        print(self.num, "/", self.den)

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __repr__(self):
        return self.__str__()

    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den

        return Fraction(newnum, newden)

    def __radd__(self, other):
        return self.add(other)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum

    def __mul__(self, other):
        num = self.num * other.num
        den = self.den * other.den
        common = gcd(num, den)
        return Fraction(num // common, den // common)

    def __truediv__(self, other):
        num = self.num * other.den
        den = self.den * other.num
        common = gcd(num, den)
        return Fraction(num // common, den // common)

    def __sub__(self, other):
        num = self.num * other.den - self.den * other.num
        den = self.den * other.den
        common = gcd(num, den)
        return Fraction(num // common, den // common)

    def __gt__(self, other):
        sub = (self - other)

        subStr = str(sub)

        if subStr[0] == "-" or subStr[0] == "0" :
            return False
        else :
            return True

    def __ge__(self, other):
        sub = (self - other)

        substr = str(sub)

        if substr[0] == "-" :
            return False
        else :
            return True

    def __lt__(self, other):
        return not (self >= other)

    def __le__(self, other):
        return not (self > other)

    def __ne__(self, other):
        return not (self == other)

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den
