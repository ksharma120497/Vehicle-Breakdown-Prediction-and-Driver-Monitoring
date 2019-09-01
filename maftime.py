import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
from datetime import timedelta
data= pd.read_csv("D:/Work/maftime.csv",low_memory=False)
print(data.shape)
data=data.fillna("0")
data.to_csv('D:/Work/maftime.csv',index=False)
print(data.isnull().sum())
maf=data['MAF']
time=data['Time']
plt.scatter(time.head(1000),maf.head(1000), color = "m", marker = "o", s = 30) 
plt.show()
