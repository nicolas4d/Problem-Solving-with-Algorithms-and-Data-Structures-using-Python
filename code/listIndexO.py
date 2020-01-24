import timeit

t = timeit.Timer("l[0]", "from __main__ import l")
for i in (10000, 1000000):
    l = range(i)
    print(t.timeit(number = 10000))


0.002006811002502218
0.002058596001006663
