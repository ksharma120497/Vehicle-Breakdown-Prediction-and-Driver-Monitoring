import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
from datetime import timedelta
#data= pd.read_csv("D:/Work/exp1_14drivers_14cars_dailyRoutes.csv",low_memory=False)
#print(data.shape)
modifiedData= pd.read_csv("D:/Work/obddataset/modifiedData.csv",low_memory=False)
modifiedData=modifiedData.fillna("0")
modifiedData.to_csv('D:/Work/obddataset/modifiedData.csv',index=False)
#print(modifiedData.isnull().sum())
maf=modifiedData['MAF']
rpm=modifiedData['ENGINE_RPM']
time=modifiedData['TIMESTAMP']
plt.scatter(maf.head(100),rpm.head(100), color = "m", marker = "o", s = 30) 
#plt.plot(maf.head(105),rpm.head(105),color="g")
plt.xlabel('MAF')
plt.ylabel('RPM')
plt.show()
