# greatest common divisor
def gcd(m,n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n

class Fraction:
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom

    def show(self):
        print(self.num,"/",self.den)

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def __add__(self,otherfraction):

        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)

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

        if subStr[0] > "-" :
            return False
        else :
            return True

    def __lt__(self, other):
        return not (self > other)

print(gcd(20,10))


myfraction = Fraction(3,5)
myfraction.show()
print(myfraction)

f1=Fraction(1,4)
f2=Fraction(1,2)
f3=f1+f2
print(f3)

mul = f1 * f2
print(mul)

div = f1 / f2
print(div)

sub = f1 - f2
print("sub", sub)

print("gt", f1 > f2)
print("lt", f1 < f2)
