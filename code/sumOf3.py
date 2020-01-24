import time

def sumOfN3(n):
    start = time.time()

    sum = (n * (n + 1)) / 2

    end = time.time()

    return sum, end - start

print(sumOfN3(10))
(55.0, 2.6226043701171875e-06)


print()

nList = [10000, 100000, 1000000, 10000000,  100000000]
for n in nList:
    print("Sum is %d required %10.7f seconds"% sumOfN3(n))

'''
Sum is 50005000 required  0.0000019 seconds
Sum is 5000050000 required  0.0000012 seconds
Sum is 500000500000 required  0.0000007 seconds
Sum is 50000005000000 required  0.0000007 seconds
Sum is 5000000050000000 required  0.0000172 seconds
'''

