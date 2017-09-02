#kaggle -titan
import pandas as pd
import numpy as np

np.random.seed(42)
from math import *
from sklearn.cross_validation import train_test_split
from sklearn.model_selection import KFold
from sklearn import svm, tree, linear_model
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn import random_projection
from extra_funct import clean
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
#training
train_in = pd.read_csv('train.csv',header=0)
test_in = pd.read_csv('test.csv',header=0)
train_in_1 = train_in
train_in = clean(train_in)

X = train_in[train_in.columns]
[X.__delitem__('SalePrice')]
Y = train_in['SalePrice']

columns = [
       'MSZoning', 'Street', 'Alley', 'LotShape', 'LandContour', 'Utilities',
       'LotConfig', 'LandSlope', 'Neighborhood', 'Condition1', 'Condition2',
       'BldgType', 'HouseStyle', 'RoofStyle', 'RoofMatl', 'Exterior1st',
       'Exterior2nd', 'MasVnrType', 'ExterQual', 'ExterCond', 'Foundation',
       'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2',
       'Heating', 'HeatingQC', 'CentralAir', 'Electrical', 'KitchenQual',
       'Functional', 'FireplaceQu', 'GarageType', 'GarageFinish', 'GarageQual',
       'GarageCond', 'PavedDrive', 'PoolQC', 'Fence', 'MiscFeature',
       'SaleType', 'SaleCondition'
]

X_1 = X
for col in columns:
   X_1 = pd.concat([X_1, pd.get_dummies(X_1[col],prefix=col)],axis=1)

[X_1.__delitem__(x) for x in columns]



X_train, X_test, y_train, y_test = train_test_split(X_1.values, Y.values, test_size=0.0)
y_train = y_train.reshape((-1, 1))
# y_test = y_test.reshape((-1, 1))
# print X_train.shape, X_test.shape, y_train.shape, y_test.shape


# #linear regression
# clf = linear_model.LinearRegression()
# clf.fit(X_train, y_train)
# print clf.score(X_test, y_test)


#-------------------------------------------------Output TEst-------------------------

Z = train_in_1
scaler_input = StandardScaler()
scaler_output = StandardScaler()
[Z.__delitem__('SalePrice')]
y_train = scaler_output.fit_transform(y_train)
test_in = clean(pd.concat([Z,test_in]))
Z = test_in[test_in.columns]

Y_1 = Z
for col in columns:
   Y_1 = pd.concat([Y_1, pd.get_dummies(Y_1[col],prefix=col)],axis=1)

[Y_1.__delitem__(x) for x in columns]
Y_2 = scaler_input.fit_transform(Y_1)
X_train = Y_2[0:1460]
Y_2 = Y_2[1460:]
Y_1 = Y_1[1460:]
#linear regression
clf = linear_model.LinearRegression()
clf.fit(X_train, y_train)
predicted = clf.predict(Y_2)
predicted = scaler_output.inverse_transform(predicted)
Y_2 = scaler_input.inverse_transform(Y_2)
out = []
for i in predicted:
	out.append(abs(i[0]))

# predicted = abs(predicted)

data = {'Id':Y_1['Id'],'SalePrice':out}
df = pd.DataFrame(data, columns = ['Id', 'SalePrice'])
df.to_csv('result.csv', sep=',')


# data = {'PassengerId':passenger_id,'Survived':predicted}
# df = pd.DataFrame(data, columns = ['PassengerId', 'Survived'])
# df.to_csv('result.csv', sep=',')
