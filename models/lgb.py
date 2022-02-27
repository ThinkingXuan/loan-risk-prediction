import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
from tqdm import tqdm
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.preprocessing import MinMaxScaler
import xgboost as xgb
import lightgbm as lgb
from catboost import CatBoostRegressor
import warnings
from sklearn.model_selection import StratifiedKFold, KFold
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score, log_loss,explained_variance_score,precision_score
warnings.filterwarnings('ignore')
import random
import pickle
from sklearn.model_selection import train_test_split
data_train = pd.read_csv('train.csv')
data_test = pd.read_csv('test.csv')

features = [f for f in data_train.columns if f not in ['cust_id','label']]
x_train = data_train[features]
x_test = data_test[features]
y_train = data_train['label']
 
train_x=x_train
train_y=y_train
test_x = x_test
 
# 用sklearn.cross_validation进行训练数据集划分，这里训练集和交叉验证集比例为7：3，可以自己根据需要设置
X, val_X, y, val_y = train_test_split(
    train_x,
    train_y,
    test_size=0.05,
    random_state=1,
    stratify=train_y ## 这里保证分割后y的比例分布与原数据一致
)
 
X_train = X
y_train = y
X_test = val_X
y_test = val_y
 
# create dataset for lightgbm
lgb_train = lgb.Dataset(X_train, y_train)
lgb_eval = lgb.Dataset(X_test, y_test, reference=lgb_train)
# specify your configurations as a dict
params = {
    'boosting_type': 'gbdt',
    'objective': 'binary',
    'metric': {'binary_logloss', 'auc'},
    'num_leaves': 10,
    'max_depth': 4,
    'min_data_in_leaf': 225,
    'learning_rate': 0.1,
    'feature_fraction': 0.9,
    'bagging_fraction': 0.95,
    'bagging_freq': 5,
    'lambda_l1': 1,  
    'lambda_l2': 0.001,  # 越小l2正则程度越高
    'min_gain_to_split': 0.2,
    'verbose': 5,
    'is_unbalance': True
}
def get_f1 (preds,dtrain):
    label=dtrain.get_label()
    preds=np.argmax(preds.reshape(len(label),-1), axis=1)
    f1=f1_score(label,preds,average='weighted')
    return 'f1-score',float(f1),True
# train
print('Start training...')
gbm = lgb.train(params,
                lgb_train,
                num_boost_round=100,
                valid_sets=lgb_eval,
                feval=get_f1,
                early_stopping_rounds=50)
 
print('Start predicting...')
 
preds = gbm.predict(test_x, num_iteration=gbm.best_iteration)  # 输出的是概率结果

#print(preds) 
label_result = pd.read_csv('label.csv')

# for j in range(1,300):
#     lgb_test_copy = np.zeros((2000,))
#     for i in range(preds.shape[0]):
#         if preds[i] > 0.001*j:
#             lgb_test_copy[i] = 1
#         else:
#             lgb_test_copy[i] = 0
#     s = roc_auc_score(label_result['label'].values, lgb_test_copy)
#     print(0.001*j,s)
for i in range(preds.shape[0]):
    if preds[i] > 0.21:
        preds[i] = 1
    else:
        preds[i] = 0
preds=pd.Series(preds)
print(preds.value_counts())
# preds=preds.astype('int')
print(f1_score(label_result['label'].values, preds))
print(precision_score(label_result['label'].values, preds))
# data_test=data_test[['cust_id']]
# data_test['label']=preds
# data_test.to_excel('./result.xlsx',index=False)
# print('********************************')
#print(f1_score(label_result['label'].values, preds))

#precision_score
