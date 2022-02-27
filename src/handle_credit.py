import pandas as pd
import datetime
data = pd.read_csv('test/handle_test_credit.csv')
#mean
# def func_term_count(data):
#     data['to_credit_lmt'] = data['credit_lmt'].mean()
#     return data
# data=data.groupby('cust_id').apply(func_term_count)

# def func_term_sum(data):
#     data['to_credit_term'] = data['credit_term'].mean()
#     return data
# data=data.groupby('cust_id').apply(func_term_sum)


# def func_DT_max(data):
#     data['maxDT'] = data['credit_etldt'].max()
#     return data
# data=data.groupby('cust_id').apply(func_DT_max)
# data['maxDT']=data.apply(lambda x: '1' if x['maxDT']==x['credit_etldt'] else '0', axis=1) 
# data=data[~data['maxDT'].isin(['0'])]
# data=data.drop(columns=['maxDT']) 


# data=data.drop(columns=['lmt_id'])
# data=data.drop(columns=['credit_etldt'])

# data['credit_actual_dt'] = pd.to_datetime(data['credit_actual_dt'],format='%Y%m%d')
# startdate = datetime.datetime.strptime('2019-03-01 01:01:01', '%Y-%m-%d %H:%M:%S')
# data['credit_actual_dt'] = data['credit_actual_dt'].apply(lambda x: x-startdate).dt.days

# data['credit_mat_dt'] = pd.to_datetime(data['credit_mat_dt'],format='%Y%m%d')
# startdate = datetime.datetime.strptime('2019-03-01 01:01:01', '%Y-%m-%d %H:%M:%S')
# data['credit_mat_dt'] = data['credit_mat_dt'].apply(lambda x: x-startdate).dt.days

data=data.drop(columns=['credit_etldt2'])
data=data.drop_duplicates()
data.to_csv('./test/handle_test_credit.csv',index=False)