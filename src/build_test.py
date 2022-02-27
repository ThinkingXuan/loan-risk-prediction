import pandas as pd
import datetime
import numpy as np
from sklearn.model_selection import train_test_split
data = pd.read_csv('merge.csv')
data1=data[0:9000]
data2=data[9000:10000]
y1=data1[['cust_id','label']]
x1=data1.drop(columns=['label'])
X_train, X_test, y_train, y_test = train_test_split( x1, y1, test_size=0.06, random_state=42)

y2=data2[['cust_id','label']]
x2=data2.drop(columns=['label'])
X2_train, X2_test, y2_train, y2_test = train_test_split( x2, y2, test_size=0.5, random_state=42)


X_train = pd.concat([X_train,X2_train],ignore_index=True)
X_test = pd.concat([X_test,X2_test],ignore_index=True)



y_train = pd.concat([y_train,y2_train],ignore_index=True)
y_test = pd.concat([y_test,y2_test],ignore_index=True)

train=pd.merge(X_train,y_train,on=['cust_id'])
test=pd.merge(X_test,y_test,on=['cust_id'])
train.to_csv('./train.csv',index=False)
test[['cust_id','label']].to_csv('./label.csv',index=False)
test=test.drop(columns=['label'])
test.to_csv('./test.csv',index=False)

print(test)

