import pandas as pd
import datetime
handle_apply = pd.read_csv('test/handle_test_apply.csv')
handle_credit = pd.read_csv('test/handle_test_credit.csv')
handle_customer_information = pd.read_csv('test/handle_test_customer_information.csv')
handle_presentation = pd.read_csv('test/handle_test_presentation.csv')
handle_flow_chart = pd.read_csv('test/handle_test_flow_chart.csv')

data=pd.merge(handle_customer_information,handle_apply,on=['cust_id'])
data=pd.merge(data,handle_credit,on=['cust_id'])
data=pd.merge(data,handle_presentation,on=['cust_id'])
data=pd.merge(data,handle_flow_chart,on=['cust_id'])
data.to_csv('./test/test_merge.csv',index=False,encoding='utf_8_sig')