# Example 1

In this example, the network should learn a simple polynomial on the interval [-2, 3]:

```
def f(x):
    return x**3 - 2 * x**2 - x
```

### Dense Netowrk

In this file, I've implemented a simple multi-layer network with a polynomial activation function. So the result is very accurate.

### LSTM and CNN networks

Using simple 1-dimensional data for these networks is not the best choice, but we've tested these architectures for our function approximation task. Both of the models have been converged to the real function.
