from timeit import Timer
import timeit

def test1():
    l = []

    for i in range(1000):
        l = l + [i]

def test2():
    l = []

    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))

t1 = Timer("test1()", "from __main__ import test1")
print("concat ", t1.timeit(number = 1000), "milliseconds")

t2 = Timer("test2()", "from __main__ import test2")
print("append ", t2.timeit(number = 1000), "milliseconds")

t3 = Timer("test3()", "from __main__ import test3")
print("comprehension ",t3.timeit(number=1000), "milliseconds")

t4 = Timer("test4()", "from __main__ import test4")
print("list range ",t4.timeit(number=1000), "milliseconds")

'''
concat  1.9212314629985485 milliseconds
append  0.11154902799171396 milliseconds
comprehension  0.08321532802074216 milliseconds
list range  0.04348137401393615 milliseconds
'''

print()

popzero = timeit.Timer("x.pop(0)",
                       "from __main__ import x")
popend = timeit.Timer("x.pop()",
                      "from __main__ import x")

x = list(range(2000000))
print(popzero.timeit(number = 1000))
print(popend.timeit(number = 1000))
'''
2.2479031140101142
0.0001133740006480366
'''

print()

popzero = timeit.Timer("x.pop(0)",
                       "from __main__ import x")
popend = timeit.Timer("x.pop()",
                      "from __main__ import x")

print("pop(0)      pop()")

for i in range(1000000, 100000001, 1000000):
    x = list(range(i))
    pt = popend.timeit(number = 1000)

    x = list(range(i))
    pz = popzero.timeit(number = 1000)

    print("%15.5f, %15.5f" % (pz, pt))

'''
pop(0)      pop()
        1.08527,         0.00012
        2.12122,         0.00012
        3.39723,         0.00012
        4.84905,         0.00012
        5.74434,         0.00014
        7.89297,         0.00012
        8.79864,         0.00015
        9.87548,         0.00020
       11.18571,         0.00013
       11.47696,         0.00013
       12.45400,         0.00012
       13.58474,         0.00012
       14.76426,         0.00012
       15.54733,         0.00013
       16.49815,         0.00013
       17.85632,         0.00013
       19.06903,         0.00013
       20.21404,         0.00013
       21.25307,         0.00013
'''
