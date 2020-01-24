import timeit
import random

for i in range(10000, 1000001, 20000):
    t = timeit.Timer("random.randrange(%d) in x" % i,
                     "from __main__ import random, x")

    x = list(range(i))
    list_time = t.timeit(number = 1000)

    x = {j : None for j in range(i)}
    d_time = t.timeit(number = 1000)

    print("%d, %10.3f, %10.3f" % (i,list_time, d_time))

'''
10000,      0.106,      0.003
30000,      0.319,      0.001
50000,      0.528,      0.002
70000,      0.763,      0.002
90000,      0.947,      0.002
110000,      1.147,      0.002
130000,      1.374,      0.002
150000,      1.542,      0.002
170000,      1.810,      0.002
190000,      2.030,      0.002
210000,      2.341,      0.002
230000,      2.496,      0.002
250000,      2.836,      0.002
270000,      3.068,      0.002
'''
