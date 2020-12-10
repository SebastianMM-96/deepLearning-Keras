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

# Compiling the previous built model
model.compile(optimizer="adam", loss="mse")

# Training
model.fit(X_train, y_train, epochs=5)

# Predicting
## predict on new data
preds = model.predict(X_test)

## look at the predictions
print(preds)

# Evaluating
## Evaluate the results
model.evaluate(X_test, y_test)