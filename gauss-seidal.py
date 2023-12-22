import numpy as np
import sys
import pandas as pd

equations = np.array([
    [1, -2, 1, 0],
    [2, 1, -3, 5],
    [4, -7, 1, -1]
])

df = pd.DataFrame(equations)

coff = df[0][1]/df[0][0]
for i in range(0,4):
    df[i][1] = df[i][1] - coff*df[i][0]

coff = df[0][2]/df[0][0]
for i in range(4):
  df[i][2] = df[i][2] - coff*df[i][0]

coff=df[1][2]/df[1][1]
for i in range(4):
    df[i][2] = df[i][2] - coff*df[i][1]

# using backward subsitution
z = df[3][2]/df[2][2]
y = (df[3][1]-df[2][1]*z)/df[1][1]
x = (df[3][0]-df[2][0]*z-df[1][0]*y)/df[0][0]
print('\n')
print(f'X: {x}\nY: {y}\nZ: {z}')
sys.exit(0)