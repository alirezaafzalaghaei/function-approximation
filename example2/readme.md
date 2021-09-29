# Example 2

In this example, the network should learn a multivariate function on the interval [-3, 3]x[-3, 3]:

```
def f(x, t):
    return np.sin(x+t)
```

### Dense Netowrk

In this file, I've implemented a simple multi-layer network for learning the function dynamics. Before that, the data was reshaped to an appropriate one. You may reshape the data such that the temporal space can be discretized into different parts. Each part should be learned by a different neural network.

### LSTM and CNN networks

These models are not implemented yet :) I recommend you use these hints for implementing the models:

- Hint 1: Maybe you can use Conv2D architecture, or reshaping the data into an appropriate one, then using Conv1D.
- Hint 2: For the LSTM model, you can reshape the data so that the model use the time variable same as a time series (i.e. a sentence)
