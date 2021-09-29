import numpy as np



def f(x):
    return np.array([np.exp(x), np.sin(x) + 3])
    

a, b = -3, 3

X = np.linspace(a, b, 1000)

Y = f(X).T
