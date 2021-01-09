import boto3

ec2 = boto3.resource('ec2')

for instance in ec2.instances.all():
    print('id: ', instance.id)
    print('name:', instance.tags[0]['Value'])
