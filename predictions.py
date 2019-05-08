#!/usr/bin/python3

import numpy as np
import pandas as pd
# from sklearn import datasets
# import seaborn as sns
# from sklearn.feature_selection import RFE
# from sklearn.model_selection import train_test_split
# from sklearn.model_selection import cross_val_score
# from sklearn.model_selection import KFold
# from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
# import matplotlib.pyplot as plt

# from sklearn.linear_model import LinearRegression
# from sklearn.linear_model import Lasso
# from sklearn.linear_model import ElasticNet
# from sklearn.tree import DecisionTreeRegressor
# from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import GradientBoostingRegressor

# from sklearn.model_selection import GridSearchCV

# from sklearn.metrics import mean_squared_error

import data_process

def get_model_scaler(X_train, Y_train):
    scaler = StandardScaler().fit(X_train)
    rescaled_X_train = scaler.transform(X_train)
    model = GradientBoostingRegressor(random_state=21, n_estimators=100)
    model.fit(rescaled_X_train, Y_train)
    return model, scaler

def predict_batch(model, scaler, X_test):
    rescaled_X_test = scaler.transform(X_test)
    predictions = model.predict(rescaled_X_test)
    return predictions
