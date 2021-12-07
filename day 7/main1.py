import numpy as np
from numpy.lib.function_base import median

inp = open('in.txt', 'r')
a = np.array(inp.read().split(','), dtype=int)
inp.close()

print(a)

most_freq = median(a)
print(most_freq)

b = np.empty_like(a)
for i in range(len(a)):
    b[i] = (abs(most_freq-a[i]))

print(b.sum())
