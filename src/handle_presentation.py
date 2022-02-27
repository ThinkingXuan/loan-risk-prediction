import pandas as pd
import datetime
data = pd.read_csv('test/test_presentation.txt')

#去重
data=data.drop(columns=['business_dt'])
data=data.drop_duplicates()
def func_term_count(data):
    data['to_term'] = data['contr_id'].count()
    return data
data=data.groupby('cust_id').apply(func_term_count)
data=data.drop_duplicates()

# # # #去重，下一个付息日
data=data.drop(columns=['next_pay_int_dt'])
data=data.drop(columns=[' loan_bal'])
data=data.drop(columns=['loan_term'])
data=data.drop_duplicates()

data=data.drop(columns=['mat_dt'])
data=data.drop(columns=['draw_dt'])

data=data.drop_duplicates()
data['prin_overdue_count']=data.apply(lambda x: int('0') if x['prin_overdue_dt']=='\\N' else int('1'), axis=1)
data=data.drop(columns=['prin_repay_freq '])
def func_overdue_count(data):
    data['overdue_term'] =data['overdue_term']+data['prin_overdue_count'].sum()
    return data
data=data.groupby('contr_id').apply(func_overdue_count)

data['to_overdue_term']=data.apply(lambda x: int(x['outsheet_term'])+int(x['overdue_term']), axis=1)
data=data.drop(columns=['prin_overdue_dt'])
data=data.drop(columns=['outsheet_term'])
data=data.drop(columns=['overdue_term'])
data=data.drop_duplicates()
data['overdue_loan_bal']=data.apply(lambda x: float(x['overdue_loan_bal'])*(int(x['overdue'])*0.04+x['overdue_grace']*0.02+1), axis=1)

data=data.drop(columns=['overdue'])
data=data.drop(columns=['overdue_grace'])
data=data.drop_duplicates()


def func_rate_mean(data):
    data['loan_used_rate'] = data['loan_used_rate'].mean()
    return data
data=data.groupby('contr_id').apply(func_rate_mean)
def func_in_pay_max(data):
    data['in_pay_amt'] = data['in_pay_amt'].max()
    return data
data=data.groupby('contr_id').apply(func_in_pay_max)
def func_out_pay_max(data):
    data['out_pay_amt'] = data['out_pay_amt'].max()
    return data
data=data.groupby('contr_id').apply(func_out_pay_max)
def func_term_max(data):
    data['max_overdue_loan_bal'] = data['overdue_loan_bal'].max()
    return data
data=data.groupby('contr_id').apply(func_term_max)
data=data.drop(columns=['overdue_loan_bal'])
data=data.drop_duplicates()
def func_uverdue_term_max(data):
    data['to_overdue_term'] = data['to_overdue_term'].max()
    return data
data=data.groupby('contr_id').apply(func_uverdue_term_max)
data=data.drop(columns=['prin_overdue_count'])

def func_term_count(data):
    data['to_contr'] = data['contr_id'].count()
    return data
data=data.groupby('cust_id').apply(func_term_count)
data=data.drop(columns=['contr_id'])
data=data.drop_duplicates()


def func_rate_mean(data):
    data['loan_used_rate'] = data['loan_used_rate'].mean()
    return data
data=data.groupby('cust_id').apply(func_rate_mean)
def func_draw_amt_mean(data):
    data['draw_amt'] = data['draw_amt'].mean()
    return data
data=data.groupby('cust_id').apply(func_draw_amt_mean)
def func_in_pay_amt_mean(data):
    data['in_pay_amt'] = data['in_pay_amt'].mean()
    return data
data=data.groupby('cust_id').apply(func_in_pay_amt_mean)
def func_out_pay_amt_mean(data):
    data['out_pay_amt'] = data['out_pay_amt'].mean()
    return data
data=data.groupby('cust_id').apply(func_out_pay_amt_mean)
def func_term_sum(data):
    data['max_overdue_loan_bal'] = data['max_overdue_loan_bal'].sum()
    return data
data=data.groupby('cust_id').apply(func_term_sum)
def func_uverdue_term_sum(data):
    data['to_overdue_term'] = data['to_overdue_term'].sum()
    return data
data=data.groupby('cust_id').apply(func_uverdue_term_sum)
data=data.drop_duplicates()

data.to_csv('./test/handle_test_presentation.csv',index=False)
# 去不要的，去重
# 按cust_id进行统计去除contr_id
# 要放款金额Draw_amt,sum

