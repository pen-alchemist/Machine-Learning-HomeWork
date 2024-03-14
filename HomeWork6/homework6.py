import numpy as np

from keras.datasets import mnist
from keras.datasets import cifar10
from keras.src.utils import to_categorical

from sklearn import preprocessing
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import normalize


def dataset_selecting(labels, features):
    """Returns dict with x_train and y_train if y >= 5 or y < 5"""
    x_train, y_train = list(), list()

    for label_ind in range(len(labels)):
        label = labels[label_ind]

        if label >= 5 or label < 5:
            y_train.append(label)
            x_train.append(features[label_ind])

    y_train = np.asarray(y_train)
    x_train = np.asarray(x_train)

    return x_train, y_train


# Load data MNIST
(x_train, y_train), (x_test, y_test) = mnist.load_data()

print(f'Training Data: {x_train.shape}')
print(f'Training Labels: {y_train.shape}')
print(f'Labels: {y_train}')

x_train, y_train = dataset_selecting(y_train, x_train)

x_train = x_train.flatten()
x_test = x_test.flatten()

x_train = x_train.reshape(len(x_train), 1)
x_test = x_test.reshape(len(x_test), 1)

# Normalizing data to 0,1
x_train = normalize(x_train)
x_test = normalize(x_test)

# One hot encode labels
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# Confirm scale of pixels
print(f'Train min={x_train.min()} max={x_train.max()}')
print(f'Test min={x_test.min()} max={x_test.max()}')

# Model making
model = LogisticRegression(random_state=42, max_iter=100000)
model.fit(x_train, y_train)
predict = model.predict(x_test)

print(f'Predict of logistic regression is: {predict}')

# Load data CIFAR10
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

print(f'Training Data: {x_train.shape}')
print(f'Training Labels: {y_train.shape}')
print(f'Labels: {y_train}')

x_train, y_train = dataset_selecting(y_train, x_train)

# Let's say, components = 2
pca = PCA(n_components=2)
pca.fit(x_train)
x_pca_train = pca.transform(x_train)
x_pca_test = pca.transform(x_test)

# Normalizing data to 0,1
x_train = normalize(x_train)
x_test = normalize(x_test)

# Confirm scale of pixels
print(f'Train min={x_train.min()} max={x_train.max()}')
print(f'Test min={x_test.min()} max={x_test.max()}')

# Encoding labels
lab_enc = preprocessing.LabelEncoder()
y_train = lab_enc.fit_transform(y_train)
y_test = lab_enc.transform(y_test)

# Model making
model = LogisticRegression(random_state=42, max_iter=100000)
model.fit(x_train, y_train)
predict = model.predict(x_test)

print(f'Predict of logistic regression is: {predict}')