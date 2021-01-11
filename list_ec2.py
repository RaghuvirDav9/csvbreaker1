import boto3

"""     this function connects to aws using boto3 and saved configuration for aws 
        and lists the name and id of all instances running in default region            """


def listInstanceNameAWS():
    ec2 = boto3.resource('ec2')
    for instance in ec2.instances.all():
        print('id: ', instance.id)
        print('name:', instance.tags[0]['Value'])


listInstanceNameAWS()
