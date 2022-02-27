import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB

data_train = pd.read_csv('merge.csv')
data_test = pd.read_csv('test/test_merge.csv')
features = [f for f in data_train.columns if f not in ['cust_id','label']]
x_train = data_train[features]
x_test = data_test[features]
y_train = data_train['label']

clf = GaussianNB()
clf.fit(x_train,y_train)
predictions = clf.predict(x_test)

# print(predictions)
# label_result = pd.read_csv('label.csv')
# # print('********************************')
# print(f1_score(label_result['label'].values, predictions))

predictions=predictions.astype('int')
data_test=data_test[['cust_id']]
data_test['label']=predictions
data_test.to_excel('./result.xlsx',index=False)
print('********************************')