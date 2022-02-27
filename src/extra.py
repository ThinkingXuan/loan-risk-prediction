import pandas as pd
import datetime
data = pd.read_csv('presentation.txt')

data=data[['cust_id','draw_dt','mat_dt']]
data=data.drop_duplicates()

data['draw_dt'] = pd.to_datetime(data['draw_dt'],format='%Y%m%d')
startdate = datetime.datetime.strptime('2019-03-01 01:01:01', '%Y-%m-%d %H:%M:%S')
data['draw_dt'] = data['draw_dt'].apply(lambda x: x-startdate).dt.days

data['mat_dt'] = pd.to_datetime(data['mat_dt'],format='%Y%m%d')
data['mat_dt'] = data['mat_dt'].apply(lambda x: x-startdate).dt.days

data['duedt']=data['draw_dt']-data['mat_dt']


def func_DT_max(data):
     data['maxDT'] = data['draw_dt'].max()
     return data
data=data.groupby('cust_id').apply(func_DT_max)
data['maxDT']=data.apply(lambda x: '1' if x['maxDT']==x['draw_dt'] else '0', axis=1) 
data=data[~data['maxDT'].isin(['0'])]
data=data.drop(columns=['maxDT']) 
data=data.drop_duplicates()


def func_DT_max(data):
     data['maxDT'] = data['mat_dt'].max()
     return data
data=data.groupby('cust_id').apply(func_DT_max)
data['maxDT']=data.apply(lambda x: '1' if x['maxDT']==x['mat_dt'] else '0', axis=1) 
data=data[~data['maxDT'].isin(['0'])]
data=data.drop(columns=['maxDT']) 
data=data.drop_duplicates()

merge = pd.read_csv('./merge.csv')
data=pd.merge(merge,data,on=['cust_id'])

data.to_csv('./merge.csv',index=False,encoding='utf_8_sig')