# Scikit Learn in Python


# Importing required packages.
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn import svm
from sklearn.neural_network import MLPClassifier
# from sklearn.linear_module import SGDClassifier
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn import preprocessing


# Loading dataset ~
wine = pd.read_csv("winequality-red.csv", sep=";")
# print(wine)
# print(wine.head())
# print(wine.isnull().sum())


"""
X_train = np.array([[1., -1.,  2.],
                    [2.,  0.,  0.],
                    [0.,  1., -1.]])
scaler = preprocessing.StandardScaler().fit(X_train)
scaler
StandardScaler()
print(scaler)
"""
