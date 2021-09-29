import numpy as np



def f(x):
    return x**3-2*x**2-x
    

a, b = -2, 3

t = np.linspace(a, b, 1000)
y = f(t)

X = t.reshape(-1, 1)
