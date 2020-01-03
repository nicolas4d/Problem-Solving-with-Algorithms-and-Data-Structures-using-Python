import time

def sumOfN3(n):
    start = time.time()
    sum = (n*(n+1))/2
    end = time.time()

    return sum, end - start

print(sumOfN3(10))

nList = [10000, 100000, 1000000, 10000000,  100000000]
for n in nList:
    print("Sum is %d required %10.7f seconds"% sumOfN3(n))
