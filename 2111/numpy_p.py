# NumPy --> pip install numpy
import numpy as np

liste = [1,2,3,4,5,6]

arr = np.array([6,5,4,6,3,5])
matrix = np.array([[3,4,"5"],[7,9,0]])
print(arr)
print(matrix)

# Array creators
zarr = np.zeros(5)
oarr = np.ones(5)

print(zarr)
print(oarr)

zmarr = np.zeros((2,3))
omarr = np.ones((3,3))

print(zmarr)
print(omarr)

arnArray = np.arange(0,10,2)
print(arnArray)

# Array Operations(Vectorized)
a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b)
print(a*b)
print(a**2)

# Basic Math & Statistics Methoden
arr = np.array([2,3,5,6,7])

print(arr.sum())
print(arr.mean()) 
print(arr.std()) #Standartabweichnung

# Zufallszahlen
print('*'*30)
print(np.random.rand(3,2)) # [0,1)
print('*'*40)
print(np.random.randn(3,3))
print('*'*40)
print(np.random.randint(1,10, size=5))