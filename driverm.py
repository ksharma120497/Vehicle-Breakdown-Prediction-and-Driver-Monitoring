import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
from datetime import timedelta
import boto3
data= pd.read_csv("D:/Work/obddataset/accelerations.csv",low_memory=False)
data2=pd.read_csv("D:/Work/obddataset/modifiedData.csv",low_memory=False)
print(data.shape)
x=data['x_value']
y=data['y_value']
ys=data2['SPEED']
count=0
counts=0
L=""
for i in range(1,1000):
    if abs(x[i+1]-x[i])>0.02 or abs(y[i+1]-y[i])>0.02:
        count=count+1

for i in range(1,1000):
    if abs(ys[i+1]-ys[i])>40:
        counts=counts+1        

if count>5 and counts<5:
    L="Reckless\nThe acceleration difference is greater than 0.02 m/s2 in x-axis\nPlease maintain Acceleration\nHappy Driving :)"
elif counts>5 and count<5:
    L="Reckless\nThe speed difference is greater than 30 m/s \nPlease slow down\nHappy Driving :)"
elif count>5 and counts>5:
    L="Reckless\nThe acceleration difference is greater than 0.01 m/s2 in x-axis\nPlease maintain Acceleration\nThe speed difference is greater than 10 m/s \nPlease slow down\nHappy Driving :)"
else:
    L="Normal\nGood Going"
s32 = boto3.resource('s3', aws_access_key_id='AKIAWXACIYAT3C5BOQLD',
        aws_secret_access_key= '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',
                                  region_name='us-west-2')
file1 = open("D:/Work/driver.txt","w")
file1.write(L) 
file1.close()
s32.meta.client.upload_file('D:/Work/driver.txt',
                           'drivermonitoring-userfiles-mobilehub-254200597',
                           'kapil/{}'.format('driver.txt'))
 
