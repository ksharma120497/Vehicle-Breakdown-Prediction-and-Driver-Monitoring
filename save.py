import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
import boto3
import json
import decimal
import time
def estimate_coef(x, y): 
	n = np.size(x) 
	m_x, m_y = np.mean(x), np.mean(y) 
	SS_xy = np.sum(y*x) - n*m_y*m_x 
	SS_xx = np.sum(x*x) - n*m_x*m_x 
	b_1 = SS_xy / SS_xx 
	b_0 = m_y - b_1*m_x 
	return(b_0, b_1) 
def plot_regression_line(x, y, b):  
	plt.scatter(x, y, color = "m", 
			marker = "o", s = 30) 
	y_pred = b[0] + b[1]*x 
	plt.plot(x, y_pred, color = "g") 
	plt.xlabel('x') 
	plt.ylabel('y') 
	plt.show()
	plt.savefig('C:/Users/kshar/Downloads/Project/Final.png')

def test(y,b):
        x1=(y-b[0])/b[1]
        s32 = boto3.resource('s3', aws_access_key_id='AKIAWXACIYAT3C5BOQLD',
        aws_secret_access_key= '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',
                                  region_name='us-west-2')
        
        

        file1 = open("D:/Work/date.txt","w")
        L=time.ctime(x1)
        file1.write(L) 
        file1.close()

        s32.meta.client.upload_file('D:/Work/date.txt',
                           'drivermonitoring-userfiles-mobilehub-254200597',
                           'kapil/{}'.format('date.txt'))
        
        
def main(): 
        data= pd.read_csv("D:/Work/obddataset/maftime.csv",low_memory=False)
        print(data.shape)
        print(data.isnull().sum())
        x=data['Time']
        y=data['MAF']
        b = estimate_coef(x, y)
        print("Estimated coefficients:\nb_0 = {}\nb_1 = {}".format(b[0], b[1]))  
        plot_regression_line(x, y, b)
        test(0,b)
        s3= boto3.resource('s3', aws_access_key_id='AKIAWXACIYAT3C5BOQLD',
        aws_secret_access_key= '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', region_name='us-east-1')
        for bucket in s3.buckets.all():
                print(bucket.name)
        s3.meta.client.upload_file('C:/Users/kshar/Downloads/Project/Figure_6.png',
                           'drivermonitoring-userfiles-mobilehub-254200597',
                           'kapil/{}'.format('Final.png'))
        
if __name__ == "__main__": 
	main()
