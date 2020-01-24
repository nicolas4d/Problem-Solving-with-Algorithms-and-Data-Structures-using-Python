import time

def sumOfN2(n):
    start = time.time()
    theSum = 0

    for i in range(1, n + 1):
        theSum = theSum + i

    end = time.time()

    return theSum, end - start

print(sumOfN2(10))
(55, 4.0531158447265625e-06)

for i in range(5):
       print("Sum is %d required %10.7f seconds" % sumOfN2(10000))

for i in range(5):
       print("Sum is %d required %10.7f seconds" % sumOfN2(100000))

for i in range(5):
       print("Sum is %d required %10.7f seconds"% sumOfN2(1000000))

'''
Sum is 50005000 required  0.0014832 seconds
Sum is 50005000 required  0.0014727 seconds
Sum is 50005000 required  0.0015764 seconds
Sum is 50005000 required  0.0017657 seconds
Sum is 50005000 required  0.0010669 seconds
Sum is 5000050000 required  0.0093143 seconds
Sum is 5000050000 required  0.0081272 seconds
Sum is 5000050000 required  0.0078387 seconds
Sum is 5000050000 required  0.0116329 seconds
Sum is 5000050000 required  0.0102496 seconds
Sum is 500000500000 required  0.1058321 seconds
Sum is 500000500000 required  0.1365056 seconds
Sum is 500000500000 required  0.1028903 seconds
Sum is 500000500000 required  0.0988216 seconds
Sum is 500000500000 required  0.1115706 seconds
'''
