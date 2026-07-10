# %%
# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load
# Install the compatible version of protobuf
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

X_train = pd.read_csv("train.csv")
X_test = pd.read_csv("test.csv")
# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All"
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session
# %%
X_train
# %%
X_train.shape
# %%
y_train = X_train.pop("label")
# %%
y_train = np.array(pd.get_dummies(y_train, dtype="float"))
# %%
import tensorflow as tf

# %%
from tensorflow.keras import Sequential

# %%
model = Sequential()
# %%
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import Input
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Flatten

# %%
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import Input
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Flatten

# %%
X_train.shape
X_train = np.array(X_train).reshape(X_train.shape[0], 28, 28, 1)
X_train = X_train / 255
print(X_test)
# y_test =X_test.pop('label')
X_test = np.array(X_test).reshape(X_test.shape[0], 28, 28, 1)
X_test = X_test / 255
# %%
model.add(Conv2D(64, kernel_size=(3, 3), activation="relu"))
# %%
model.add(Conv2D(64, kernel_size=(3, 3), activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

# flatten and put a fully connected layer
model.add(Flatten())
model.add(Dense(256, activation="relu"))  # fully connected
model.add(Dropout(0.5))

# softmax layer
model.add(Dense(10, activation="softmax"))
model.compile(loss="categorical_crossentropy", metrics=["accuracy"], optimizer="adam")
# model summary
model.summary()


early_stopping = tf.keras.callbacks.EarlyStopping(
    monitor="loss", mode="min", patience=7, restore_best_weights=True
)
# %%
model.fit(X_train, y_train, epochs=100, batch_size=128, callbacks=early_stopping)
# %%
y_pred = model.predict(X_test)
# %%
y_pred = pd.DataFrame(np.argmax(y_pred, axis=1))
# %%
y_pred = pd.DataFrame({"ImageId": range(1, y_pred.shape[0] + 1), "Label": y_pred[0]})
y_pred.to_csv("submission.csv", index=False)
y_pred
