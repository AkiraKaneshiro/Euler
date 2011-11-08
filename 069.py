import numpy as np
from collections import defaultdict

def factors(n):
    result = []
    for i in range(1, n+1):
        div = n / i
        if div < i:
            break
        if div * i != n:
            continue
        if div == i:
            result.append(i)
        else:
            result.extend([i, div])
    return set(result)

dict = {}
facts = defaultdict(list)
HI = 1000001
for i in range(2, HI):
    if i % 10000 == 0:
        print i
    dict[i] = np.arange(i, HI, i)
    for d in dict[i]:
        facts[d].append(i)

coprime = np.ones(HI+2, dtype='bool')
p = np.zeros(HI+2)
pn = np.zeros(HI+2)
for i in range(1, HI):
    if i % 10000 == 0:
        print i
    coprime[:] = True
    coprime[0] = False
    for f in facts[i]:
        coprime[dict[f]] = False
    p[i] = np.sum(coprime[1:i])
    if i == 1: continue
    pn[i] = i / p[i]

print pn.max(), pn.argmax()
    
    
