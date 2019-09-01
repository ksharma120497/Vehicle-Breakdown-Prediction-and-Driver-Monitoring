import pandas as pd
data= pd.read_csv("D:/Work/obddataset/maftime.csv",low_memory=False)
data=data.fillna("0")
data.to_csv('D:/Work/obddataset/maftime.csv',index=False)
print(modifiedData.isnull().sum())
