import boto3
import click

"""     this function connects to aws using boto3 and saved configuration for aws 
        and lists the name and id of all instances running in default region            """


@click.command()
@click.option("--state", default='ALL', help="Number of greetings.")
def listInstanceNameAWS(state: str) -> None:
    ec2 = boto3.resource('ec2')
    if state == 'running':
        for instance in ec2.instances.all():
            if instance.state['Name'] == 'running':
                print('Printing just running instances')
                print('id: ', instance.id)
                print('name:', instance.tags[0]['Value'])
                print('state:',instance.state['Name'])
                print()
    else:
        for instance in ec2.instances.all():
            print('id: ', instance.id)
            print('state:',instance.state['Name'])
            print('name:', instance.tags[0]['Value'])
            print()


listInstanceNameAWS()
