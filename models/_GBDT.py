import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score
from sklearn.ensemble import GradientBoostingClassifier

data_train = pd.read_csv('train.csv')
data_test = pd.read_csv('test.csv')
features = [f for f in data_train.columns if f not in ['cust_id','label']]
x_train = data_train[features]
x_test = data_test[features]
y_train = data_train['label']

clf = GradientBoostingClassifier(n_estimators=200)
clf.fit(x_train,y_train)
predictions = clf.predict(x_test)

for i in range(predictions.shape[0]):
    print(i,predictions[i])
label_result = pd.read_csv('label.csv')
# print('********************************')
print(f1_score(label_result['label'].values, predictions))