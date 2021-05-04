# CNN Model trained on image data to predict new image data classification

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.preprocessing import image_dataset_from_directory
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D, BatchNormalization

# Reference: https://www.geeksforgeeks.org/cnn-image-data-pre-processing-with-generators/
# Reference: https://keras.io/api/preprocessing/image/
# Reference: https://www.tensorflow.org/guide/data



# Using tensorflow.keras.preprocessing.image_dataset_from_directory to read in image data.  Images are classified by the directory folders they are in automatically.  Original image size is retained.  95 images, 8 classes.
image_data = image_dataset_from_directory('../assets',
                                        labels='inferred',
                                        label_mode='categorical',
                                        image_size=(255, 350),
                                        batch_size=204,
                                        shuffle=False)

# using for loop to separate image data from class data.  numpy.copy converts data to arrays.
for img in image_data:
    X = np.copy(img[0])
    y = np.copy(img[1])

# transforming image data from values between 0 and 255 to values between 0 and 1.
X /= 255

# splitting data into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.25,
                                                    random_state=420,
                                                    stratify=y)


# instantiating model
cnn_model = Sequential()

# add filters to image data through Conv2D and pool filtered image data with MaxPooling2D to reduce complexity.
cnn_model.add(Conv2D(filters=32,
                     kernel_size=(3,3),
                     activation='relu',
                     input_shape=(255, 350, 3)
                ))
cnn_model.add(MaxPooling2D(pool_size=(2,2)))

cnn_model.add(Conv2D(filters=64,
                     kernel_size=(3,3),
                     activation='relu'
                ))
cnn_model.add(MaxPooling2D(pool_size=(2,2)))

cnn_model.add(Conv2D(filters=64,
                     kernel_size=(3,3),
                     activation='relu'
                ))
cnn_model.add(MaxPooling2D(pool_size=(2,2)))

cnn_model.add(Conv2D(filters=128,
                     kernel_size=(3,3),
                     activation='relu'
                ))
cnn_model.add(MaxPooling2D(pool_size=(2,2)))

# flatten image data for input into neural network
cnn_model.add(Flatten())

# add dense layers and dropout layers to neural network

cnn_model.add(Dense(256,
                    activation='relu'
                    ))
cnn_model.add(Dropout(0.5))

cnn_model.add(Dense(512,
                    activation='relu'
                    ))
cnn_model.add(Dropout(0.4))

cnn_model.add(Dense(256,
                    activation='relu'
                    ))
cnn_model.add(Dropout(0.3))

cnn_model.add(Dense(9,
                    activation='softmax'
                    ))

# compile using categorical crossentropy and accuracy as metric
cnn_model.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy']
                  )

# Early stopping to prevent testing data from running on unnecessarily long
es = EarlyStopping(patience=10)

# training the model on training data.  validating model with testing data.
history = cnn_model.fit(X_train,
                      y_train,
                      batch_size=512,
                      validation_data=(X_test, y_test),
                      epochs=100,
                      verbose=2,
                      callbacks=[es])

# print summary of network parameters
cnn_model.summary()

# export plot for training and testing loss
plt.plot(history.history['loss'], label='Training Loss', color='orange')
plt.plot(history.history['val_loss'], label='Testing Loss', color='blue')
plt.xlabel('Epochs', fontsize=14)
plt.ylabel('Loss Percentage', fontsize=14)
plt.title('Change in Loss per Epoch', fontsize=18)
plt.legend();
plt.savefig('../data/loss.png')
plt.clf()

# export plot for training and testing accuracy
plt.plot(history.history['accuracy'], label='Training Acc.', color='red')
plt.plot(history.history['val_accuracy'], label='Testing Acc.', color='green')
plt.xlabel('Epochs', fontsize=14)
plt.ylabel('Accuracy Percentage', fontsize=14)
plt.title('Change in Accuracy per Epoch', fontsize=18)
plt.legend();
plt.savefig('../data/acc.png')

# saving model to file for use in flask application
cnn_model.save('../flask_app/model')

# loading model back in to confirm work save file
# cap_model = load_model('../flask_app/cap_model')

# cap_model.summary()
