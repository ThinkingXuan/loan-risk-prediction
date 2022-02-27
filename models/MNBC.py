import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier, VotingClassifier, RandomForestClassifier
import xgboost
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import f1_score

data_train = pd.read_csv('train.csv')
data_test = pd.read_csv('test.csv')
features = [f for f in data_train.columns if f not in ['cust_id','label']]
x_train = data_train[features]
x_test = data_test[features]
y_train = data_train['label']


clf1 = GradientBoostingClassifier(n_estimators=200)
clf2 = RandomForestClassifier(random_state=0, n_estimators=500)
clf3 = LogisticRegression(random_state=1)
clf4 = GaussianNB()
clf5 = xgboost.XGBClassifier()
clf = VotingClassifier(estimators=[
    ('gbdt',clf1),
    ('rf',clf2),
    ('lr',clf3),
    ('nb',clf4),
    ('xgboost',clf5),
    ],
    voting='soft')
clf.fit(x_train,y_train)
predictions = clf.predict(x_test)


print(predictions)
label_result = pd.read_csv('label.csv')
# print('********************************')
print(f1_score(label_result['label'].values, predictions))