# Activation functions

![image](https://goodboychan.github.io/chans_jupyter/images/copied_from_nb/image/process.png)

## An activation function

A summation of the inputs reaching the neuron multiplied by the weights of each connection and the addition of the bias weight. This operation results in a number: a, which can be anything, it is not bounded.

## An activation function

We pass this number into an activation function that essentially takes it as an input and decides how the neuron fires and which output it produces. Activation functions impact learning time, making our model converge faster or slower and achieving lower or higher accuracy. They also allow us to learn more complex functions. 

## Activation zoo

The ReLU (Rectified linear unit) which varies between 0 and infinity and the leaky ReLU, which we can look as a smoothed version of ReLU that doesn't sit at 0, allowing negative values for negative inputs