import numpy as np
import sys
import pandas as pd

equations = np.array([
    [1, 1, 1, 9],
    [2, -3, 4, 13],
    [3, 4, 5, 40]
])

df = pd.DataFrame(equations,dtype=float)

coff1 = df[0][1]/df[0][0]
coff2 = df[0][2]/df[0][0]
for i in range(4):
    df[i][1] = df[i][1] - coff1*df[i][0]
    df[i][2] = df[i][2] - coff2*df[i][0]

  
coff1=df[1][2]/df[1][1]
coff2=df[1][0]/df[1][1]
for i in range(4):
    df[i][2] = df[i][2] - coff1*df[i][1]
    df[i][0] = df[i][0] - coff2*df[i][1]

coff1=df[2][0]/df[2][2]
coff2=df[2][1]/df[2][2]
for i in range(4):
    df[i][0] = df[i][0]-coff1*df[i][2]
    df[i][1] = df[i][1]-coff2*df[i][2]

x = df[3][0]/df[0][0]
y = df[3][1]/df[1][1]
z = df[3][2]/df[2][2]
print('\n')
print(f'X: {x}\nY: {y}\nZ: {z}')
sys.exit(0)