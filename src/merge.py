import pandas as pd
import datetime
handle_apply = pd.read_csv('handle_apply.csv')
handle_credit = pd.read_csv('handle_credit.csv')
handle_customer_information = pd.read_csv('handle_customer_information.csv')
handle_presentation = pd.read_csv('handle_presentation.csv')
handle_flow_chart = pd.read_csv('handle_flow_chart.csv')

data=pd.merge(handle_customer_information,handle_apply,on=['cust_id'])
data=pd.merge(data,handle_credit,on=['cust_id'])
data=pd.merge(data,handle_presentation,on=['cust_id'])
data=pd.merge(data,handle_flow_chart,on=['cust_id'])
data.to_csv('./merge.csv',index=False,encoding='utf_8_sig')