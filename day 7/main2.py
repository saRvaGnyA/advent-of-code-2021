import numpy as np
from numpy.lib.function_base import median

inp = open('in.txt', 'r')
a = np.array(inp.read().split(','), dtype=int)
inp.close()

print(a)

most_freq = int(np.mean(a))

b = np.empty_like(a)
for i in range(len(a)):
    diff = abs(most_freq-a[i])
    b[i] = diff*(diff+1)/2

print(b.sum())
