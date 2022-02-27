import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score
from sklearn.linear_model import LogisticRegression
from sklearn import tree

data_train = pd.read_csv('train.csv')
data_test = pd.read_csv('test.csv')
features = [f for f in data_train.columns if f not in ['cust_id','label']]
x_train = data_train[features]
x_test = data_test[features]

y_train = data_train['label']

clf = tree.DecisionTreeClassifier()
clf.fit(x_train,y_train)
predictions = clf.predict(x_test)

print(predictions)
label_result = pd.read_csv('label.csv')
# print('********************************')
print(f1_score(label_result['label'].values, predictions))