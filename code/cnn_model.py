import numpy as np
import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing import image_dataset_from_directory
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D

# Reference: https://www.geeksforgeeks.org/cnn-image-data-pre-processing-with-generators/
# Reference: https://keras.io/api/preprocessing/image/
# Reference: https://www.tensorflow.org/guide/data

image_data = image_dataset_from_directory('../assets',
                                        labels='inferred',
                                        label_mode='categorical',
                                        image_size=(255, 350),
                                        shuffle=False)

for img in image_data:
    X = np.asarray(img[0])
    y = np.asarray(img[1])

X_train, X_test, y_train, y_test = train_test_split(X, y)

cnn_model = Sequential()

cnn_model.add(Conv2D(filters=16,
                     kernel_size=(3,3),
                     activation='relu',
                     input_shape=(255, 350, 3)
                ))
cnn_model.add(MaxPooling2D())
cnn_model.add(Conv2D(filters=32,
                     kernel_size=(3,3),
                     activation='relu'
                ))
cnn_model.add(MaxPooling2D())
cnn_model.add(Flatten())
cnn_model.add(Dense(32,
                    activation='relu'
                    ))
cnn_model.add(Dropout(0.5))
cnn_model.add(Dense(16,
                    activation='relu'
                    ))
cnn_model.add(Dropout(0.5))
cnn_model.add(Dense(2,
                    activation='softmax'
                    ))
cnn_model.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy']
                  )

history = cnn_model.fit(X_train,
                      y_train,
                      batch_size=128,
                      validation_data=(X_test, y_test),
                      epochs=10,
                      verbose=2)

cnn_model.save('../cap_model')

cap_model = load_model('../cap_model')

cap_model.summary()
