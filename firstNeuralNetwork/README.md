# First neural network

![Nn](https://upload.wikimedia.org/wikipedia/commons/9/99/Neural_network_example.svg)

A neural network is a machine learning algorithm with the training data being the input to the input layer and the predicted value the value at the output layer. 

## Parameters

![params](https://qph.fs.quoracdn.net/main-qimg-c63faaef309939f9bfa4887b4ed537df)

Each connection from one neuron to another has an associated weight w. Each neuron, except the input layer which just holds the input value, also has an extra weight we call the bias weight, b. During feed-forward our input gets transformed by weight multiplications and additions at each layer, the output of each neuron can also get transformed by the application of what's called an activation function. 

## Gradient descent

![gd](http://rasbt.github.io/mlxtend/user_guide/general_concepts/gradient-optimization_files/ball.png)

Learning in neural networks consists of tuning the weights or parameters to give the desired output. One way of achieving this is by using the famous gradient descent algorithm, and applying weight updates incrementally via a process known as back-propagation.

## Sequential API

![API](https://miro.medium.com/max/567/1*ytBUCmhkAucJ5imsNfAyfQ.png)