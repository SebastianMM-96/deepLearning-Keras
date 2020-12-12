import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense

irrigation = pd.read_csv('irrigation_machine.csv', index_col=0)
irrigation.head()

parcels = irrigation[['parcel_0', 'parcel_1', 'parcel_2']].to_numpy()
sensors = irrigation.drop(['parcel_0', 'parcel_1', 'parcel_2'], axis=1).to_numpy()

X_train, X_test, y_train, y_test = \
    train_test_split(sensors, parcels, test_size=0.3, stratify=parcels)

np.random.seed(1)

# Return a new model with the given activation
def get_model(act_function):
    model = Sequential()
    if act_function == 'leaky_relu':
        model.add(Dense(64, input_shape=(20, ), activation=nn.leaky_relu))
    else:
        model.add(Dense(64, input_shape=(20, ), activation=act_function))

    # Add an output layer of 3 neurons with sigmoid activation
    model.add(Dense(3, activation='sigmoid'))
    # Compile your model with binary crossentropy loss
    model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])
    return model

activations = ['relu', 'leaky_relu', 'sigmoid', 'tanh']

# Loop over the activation functions
activation_results = {}

for act in activations:
    # Get a new model with the current activation
    model = get_model(act)
    
    # Fit the model and store the history results
    h_callback = model.fit(X_train, y_train, epochs=20, validation_data=(X_test, y_test), verbose=0)
    activation_results[act] = h_callback
    print('Finishing with {}...'.format(act))

val_loss_per_function = {}
val_acc_per_function = {}

for k, v in activation_results.items():
    val_loss_per_function[k] = v.history['val_loss']
    val_acc_per_function[k] = v.history['val_accuracy']

val_loss = pd.DataFrame(val_loss_per_function)

# Call plot on the dataframe
val_loss.plot(title='validation Loss')

# Create a dataframe from val_acc_per_function
val_acc = pd.DataFrame(val_acc_per_function)

# Call plot on the dataframe
val_acc.plot(title='validation Accuracy')