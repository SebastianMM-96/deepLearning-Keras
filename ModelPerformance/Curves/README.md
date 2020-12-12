# Learning curves

## Loss curve

Loss tends to decrease as epochs go by. This is expected since our model is essentially learning to minimize the loss function. Epochs are shown on the X axis and loss on the Y-axis. As epochs go by our loss value decreases. After a certain amount of epochs, the value converges, meaning it no longer gets much lower than that. We've arrived at a minimum.

## Accuracy curve

Accuracy curves are similar but opposite in tendency if the Y-axis shows accuracy it now tends to increase as epochs go by. This shows our model makes fewer mistakes as it learns.

## Overfitting

If we plot training versus validation data we can identify overfitting. We will see the training and validation curves start to diverge. Overfitting is when our model starts learning particularities of our training data which don't generalize well on unseen data. The early stopping callback is useful to stop our model before it starts overfitting.

## Unstable curves

But not all curves are smooth and pretty, many times we will find unstable curves. There are many reasons that can lead to unstable learning curves; the chosen optimizer, learning rate, batch-size, network architecture, weight initialization, etc. All these parameters can be tuned to improve our model learning curves, as we aim for better accuracy and generalization power.