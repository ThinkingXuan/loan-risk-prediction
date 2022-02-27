import pandas as pd
import datetime
data = pd.read_csv('flow_chart.txt')
#data = data[~data['repay_dt'].isin(['\\N'])]
data['debt']=data.apply(lambda x: float('0') if x['lmt_id']=='\\N' else int(float(x['atl_rpy_fine_intr'])+float(x['atl_rpy_intr_atm'])+float(x['atl_rpy_prin_atm'])-float(x['collect_press_fee'])-float(x['tot_ap_fine_intr'])-float(x['tot_ap_intr'])-float(x['tot_ap_prin'])), axis=1)
#看客户数量
#print('类型数：', data['cust_id'].nunique())
#sum

data['type']=data.apply(lambda x: int('1') if x['repay_type']=='03' else int('0'), axis=1)
def func_term_count(data):
    data['typeCT'] = data['type'].sum()
    return data
data=data.groupby('cust_id').apply(func_term_count)

data=data[['cust_id','debt','typeCT']]
data=data.drop_duplicates()


def func_term_sum(data):
    data['debt'] = data['debt'].sum()
    return data
#print(data.groupby('cust_id').apply(lamdba x: x['contr_id'].count()))
data=data.groupby('cust_id').apply(func_term_sum)
data=data[['cust_id','typeCT','debt']]
data=data.drop_duplicates()
data.to_csv('./handle_flow_chart.csv',index=False)
#data1 = pd.read_csv('credit.txt')
#data=pd.merge(data,data1,on=['cust_id','lmt_id'])
