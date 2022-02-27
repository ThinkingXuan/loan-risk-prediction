import pandas as pd
import datetime
data = pd.read_csv('test/test_customer_information.txt')
#data['address']=data['address'].apply(lambda x:x[0:6])
data['birth'] = pd.to_datetime(data['birth'],format='%Y%m%d')
startdate = datetime.datetime.strptime('20190301', '%Y%m%d')
data['birthDT'] = data['birth'].apply(lambda x: x-startdate).dt.days
data=data.drop(columns=['birth'])
data.to_csv('./test/handle_test_customer_information.csv',index=False)