# Import's
from keras.models import Sequential
from keras.layers import Dense

# Create a new sequential model
model = Sequential()
# Add and input and dense layer
model.add(Dense(2, input_shape=(3, ), activation="relu"))
# Add a final 1 neuron layer
model.add(Dense(1))

# Summarize the model
model.summary()