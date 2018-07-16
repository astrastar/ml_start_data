import pandas as pd
import quandl
import numpy as np
from sklearn import preprocessing, svm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import MySQLdb
import math
from matplotlib import pylab as plt
import datetime
import time
import pickle

conn = MySQLdb.connect('localhost', 'root', '123456', 'btc_hour')

i = 1919
df = pd.read_sql('SELECT * from new_btc', conn)
df = df[:1960]
df = df[['open', 'close', 'high', 'low', 'volume', 'min_delta', 'max_delta']]
df['change'] = (df['close'] - df['open']) / df['open'] * 100
df = df[['open', 'close', 'high', 'low', 'volume', 'change']]
forecast_col = 'close'
forecast_out = int(math.ceil(0.01 * len(df)))
df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)

X = np.array(df.drop(['label'], 1))
X = preprocessing.scale(X)
X_l = X[-forecast_out:]
X = X[:-forecast_out]
# df.dropna(inplace=True)

y = df['label']
y = y[:-forecast_out]
y.dropna(inplace=True)
y = np.array(y)

# X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.5)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
clf = LinearRegression(n_jobs=-1)
clf.fit(X_train, y_train)
acc = clf.score(X_test, y_test)
forecast_set = clf.predict(X_l)
print(forecast_set, acc)
print(df.tail())
# print(datetime.datetime.utcfromtimestamp(1524214800))



