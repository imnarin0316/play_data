import numpy as np
a, b = map(int, input().strip().split(' '))
arr = np.full((b,a), '*')
for row in arr:
    print(''.join(row))
