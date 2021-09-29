import numpy as np



def f(x, t):
    return np.sin(x+t)
    

x0, x1 = -3, 3
t0, t1 = -3, 3

x = np.linspace(x0, x1, 500)
t = np.linspace(t0, t1, 500)

x, t = np.meshgrid(x, t)
y = f(x, t)