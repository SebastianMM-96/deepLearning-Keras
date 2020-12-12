# Keras callbacks

## What is a callback?

A callback is a function that is executed after some other function, event, or task has finished. For instance, when you touch your phone screen, a block of code that identifies the type of gesture will be triggered. Since this block of code has been called after the touching event occurred, it's a callback. 

## Callbacks in Keras

In the same way, a keras callback is a block of code that gets executed after each epoch during training or after the training is finished. They are useful to store metrics as the model trains and to make decisions as the training goes by.