# Example 3

In this example, the network should learn a vector-valued function on the interval [-3, 3]:

```
def f(x):
    return np.array([np.exp(x), np.sin(x) + 3])
```

### Dense Netowrk

In this file, I've implemented a simple multi-layer network for learning the function dynamics. The difference between this model and the first example is the number of neurons on the last layer. Here, since we need to learn two functions, we should have different neurons.

### LSTM and CNN networks

These models are not implemented yet :)
