import pandas as pd
import datetime
data = pd.read_csv('test/test_apply.txt')
data['apply_date'] = pd.to_datetime(data['apply_date'],format='%Y-%m-%d %H:%M:%S')
startdate = datetime.datetime.strptime('2019-03-01 01:01:01', '%Y-%m-%d %H:%M:%S')
data['apply_dateDT'] = data['apply_date'].apply(lambda x: x-startdate).dt.days

data['apply_amount']=data['apply_amount'].apply(lambda x: int(x)/100)
def func_DT_max(data):
    data['maxDT'] = data['apply_date'].min()
    return data
data=data.groupby('cust_id').apply(func_DT_max)
data['maxDT']=data.apply(lambda x: '1' if x['maxDT']==x['apply_date'] else '0', axis=1) 
data=data[~data['maxDT'].isin(['0'])]
data=data.drop(columns=['maxDT'])
data=data.drop(columns=['apply_date']) 
def func_DT_max(data):
    data['apply_amount'] = data['apply_amount'].max()
    return data
data=data.groupby('cust_id').apply(func_DT_max)
data=data.drop_duplicates()
data.to_csv('./test/handle_test_apply.csv',index=False)
print('类型数：', data['cust_id'].nunique())


