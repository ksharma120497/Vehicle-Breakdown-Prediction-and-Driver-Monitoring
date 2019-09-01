import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
from datetime import timedelta
#data= pd.read_csv("D:/Work/exp1_14drivers_14cars_dailyRoutes.csv",low_memory=False)
modifiedData= pd.read_csv("D:/Work/obddataset/newmaftime.csv",low_memory=False)
print(modifiedData.shape)
#modifiedData=modifiedData.fillna("0")
#modifiedData.to_csv('D:/Work/modifiedData.csv',index=False)
#print(modifiedData.isnull().sum())
maf=modifiedData['MAF']
rpm=modifiedData['RPM']
time=modifiedData['Time']
plt.scatter(maf.head(100),rpm.head(100), color = "m", marker = "o", s = 30) 
#plt.plot(maf.head(105),rpm.head(105),color="g")
plt.xlabel('RPM')
plt.ylabel('MAF')
#plt.show()
m=[]
ini=160
fin=163
l=1
sumtime=time[160]
value={'MAF':[],'Time':[]}
daf=pd.DataFrame(columns=['MAF','Time'])
for j in range(0,60000,100):
    summaf=0
    sumrpm=0
    sumrpmmaf=0
    sumrpmrpm=0
    for i in range(ini,fin):
        if maf[i] != 0:
            summaf=summaf+maf[i]
            sumrpm=sumrpm+rpm[i]
            sumrpmmaf=sumrpmmaf+(rpm[i]*maf[i])
            sumrpmrpm=sumrpmrpm+(rpm[i]*rpm[i])
    try:
        m=(sumrpmmaf-(sumrpm*summaf))/(sumrpmrpm-(sumrpm*sumrpm))
    except ZeroDivisionError:
        ini=ini+3
        fin=fin+3
        continue
    ini=ini+3
    fin=fin+3
    sumtime=sumtime+900
    daf=daf.append({'MAF':m,'Time':sumtime},ignore_index=True)
df = pd.DataFrame(data=daf,columns= ['MAF', 'Time'])
df.to_csv (r'D:/Work/obddataset/maftime.csv', index = None, header=True)
#plt.scatter(time1,m, color = "m", marker = "o", s = 30)
#plt.show()
