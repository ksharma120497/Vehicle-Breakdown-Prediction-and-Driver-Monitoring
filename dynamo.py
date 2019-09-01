import boto3
s3= boto3.resource('s3', aws_access_key_id='AKIAWXACIYAT3C5BOQLD',
         aws_secret_access_key= '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', region_name='us-east-1')
for bucket in s3.buckets.all():
    print(bucket.name)
data = open('C:/Users/kshar/Downloads/Project/Figure_1.png', 'rb')
filename='Figure_1.png'
#s3.Bucket('drivermonitoring-userfiles-mobilehub-254200597-kapil').put_object(Key='test.png',Body=data)
s3.meta.client.upload_file('C:/Users/kshar/Downloads/Project/'+filename,
                           'drivermonitoring-userfiles-mobilehub-254200597',
                           'kapil/{}'.format('test.png'))
