# Function approximation using neural networks

This repository aims to approximate a function using various deep neural network architectures. The examples may be a simple sine wave or a multivariate complex vector-valued function.

Each function can be learned with a different neural network, so we've split the repository into different folders. These directories contain a python file named `example.py` that extracts some datapoint from a known function. The jupyter notebook files use these data to learn the function.

## Repository examples

 - [x] <img src="https://render.githubusercontent.com/render/math?math=f(x): \mathbb{R}\to\mathbb{R}"> (Example-1)
 - [x] <img src="https://render.githubusercontent.com/render/math?math=f(x): \mathbb{R}^n\to\mathbb{R}"> (Example-2)
 - [x] <img src="https://render.githubusercontent.com/render/math?math=f(x): \mathbb{R}\to\mathbb{R}^m"> (Example-3)
 - [x] <img src="https://render.githubusercontent.com/render/math?math=f(x): \mathbb{R}^n\to\mathbb{R}^m"> (Example-4)
 - [ ] <img src="https://render.githubusercontent.com/render/math?math=f(x): \mathbb{C}\to\mathbb{R}">
 - [ ] <img src="https://render.githubusercontent.com/render/math?math=f(x): \mathbb{R}\to\mathbb{C}">
 - [x] <img src="https://render.githubusercontent.com/render/math?math=f(x): \mathbb{R}\to\mathbb{R}"> + Prior knowledge: `the target function is a sine wave` (Example-1: Polynomial function)

*Currently, only the first example is provided. Other examples will be added as soon as possible.

## Architectures

 - [x] Dense (MLP)
 - [x] CNN
 - [x] LSTM
 - [ ] GRU

## What's next?

 - [ ] Auto-Encoders
 - [ ] GAN
 - [ ] Transformers
 - [ ] Real Neurons ([link](https://www.nengo.ai/nengo/v3.1.0/examples/basic/many-neurons.html))
