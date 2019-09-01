import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
from datetime import timedelta
import time
data= pd.read_csv("D:/Work/obddataset/obdData.csv",low_memory=False)
print(data.shape)
obdpid=data['obdPid']
time1=data['timestamp']
data1=data['data']
tripid=data['trip_id']
count=3
maf=[]
time2=[]
timestamp=[]
rpm=[]
trip=[]
daf=pd.DataFrame(columns=['Tripid','MAF','RPM','Time'])
for i in range(1,1196375):
    if obdpid[i]=='10':
        maf.append(data1[i])
        time2=time1[i]
        obj1=time.strptime(time1[i],"%Y-%m-%d %H:%M:%S.%f")
        timestamp.append(time.mktime(obj1))
        trip.append(tripid[i])
    
    if obdpid[i]=='0C':
        rpm.append(data1[i])
       
    else:
        continue
for j in range(1,len(maf)):
    daf=daf.append({'Tripid':trip[j],'MAF':maf[j],'RPM':rpm[j],'Time':timestamp[j]},ignore_index=True)
df = pd.DataFrame(data=daf,columns= ['Tripid','MAF','RPM','Time'])
df.to_csv (r'D:/Work/obddataset/newmaftime.csv', index = None, header=True)

 
