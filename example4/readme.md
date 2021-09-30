# Example 3

In this example, the network should learn a multi-variate vector-valued function on the interval [-3, 3]:

```
def f(x, t):
    return np.array([np.exp(x - t), t**2 - x**2])
```

### Dense Netowrk

In this file, I've implemented a simple multi-layer network for learning the function dynamics. Here, the implementation is very similar to Examples 2 and 3.

### LSTM and CNN networks

These models are not implemented yet :)
