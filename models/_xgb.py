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
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score, log_loss,explained_variance_score
warnings.filterwarnings('ignore')
import random
import pickle
import xgboost
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
data_train = pd.read_csv('train.csv')
data_test = pd.read_csv('test.csv')
data_train=data_train.drop(columns=['credit_actual_dt','address','birthDT','credit_actual_dt','credit_mat_dt','credit_lmt','credit_term','to_credit_lmt'])

features = [f for f in data_train.columns if f not in ['cust_id','label']]
x_train = data_train[features]
x_test = data_test[features]
y_train = data_train['label']



clf = xgboost.XGBClassifier()
clf.fit(x_train,y_train)
predictions = clf.predict(x_test)


# for i in range(predictions.shape[0]):
#     print(i,predictions[i])

label_result = pd.read_csv('label.csv')
# # print('********************************')
print(f1_score(label_result['label'].values, predictions))

