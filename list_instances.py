import boto3
import click

"""     this function connects to aws using boto3 and saved configuration for aws
        and lists the name and id of all instances running in default region            """

cli = click.Group()


@click.command()
@click.option("--state", default='ALL', help="State of instances to be listed.")
def listInstanceNameAWS(state: str) -> list:
    ec2 = boto3.resource('ec2')
    instances = []
    if state == 'running':
        for instance in ec2.instances.all():
            if instance.state['Name'] == 'running':
                instances.append([instance.id, instance.tags[0]['Value'], instance.state['Name']])
                # pri
    elif state == 'stopped':
        for instance in ec2.instances.all():
            if instance.state['Name'] == 'stopped':
                instances.append([instance.id, instance.tags[0]['Value'], instance.state['Name']])
                # pri()

    else:
        for instance in ec2.instances.all():
            instances.append([instance.id, instance.tags[0]['Value'], instance.state['Name']])
    print(instances)
    return instances


if __name__ == '__main__':
    listInstanceNameAWS()
