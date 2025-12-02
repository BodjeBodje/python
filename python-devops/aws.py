import boto3

ec2=boto3.client("ec2")

#print the ids of all running instances.
def print_info():
    res=ec2.describe_instances()
    reservations=res["Reservations"]
    for res in reservations:
        for instance in res["Instances"]:
            
            if instance["State"]["Name"]=="running":
                print(instance["InstanceId"])
            # print(instance["InstanceId"])
            
print_info()

#create a new ec2 instance
def create_instance():
    response=ec2.run_instances(
        ImageId="ami-0c55b159cbfafe1f0",
        InstanceType="t2.micro",
        MinCount=1,#number of instances to launch
        MaxCount=1 #number of instances to launch
    )
    print(response,"Instance created successfully")
    
# create_instance()

#a function to stop an instance
def stop_instance(instance_id):
    response=ec2.stop_instances(
        InstanceIds=[
            instance_id
        ]
    )
    print(response,"Instance stopped successfully")
    
    waiter=ec2.get_waiter("instance_stopped")
    waiter.wait(InstanceIds=[instance_id])
    print("Instance is now stopped")
    
#start an instance
def start_instance(instance_id):
    response=ec2.start_instances(
        InstanceIds=[
            instance_id
        ]
    )
    print(response,"Instance started successfully")
    
    waiter=ec2.get_waiter("instance_running")
    waiter.wait(InstanceIds=[instance_id])
    print("Instance is now running")
# start_instance("i-0d3f4e5b6c7d8e9f0")

#terminate an instance
def terminate_instance(instance_id):
    response=ec2.terminate_instances(
        InstanceIds=[
            instance_id
        ]
    )
    print(response,"Instance terminated successfully")
    
    waiter=ec2.get_waiter("instance_terminated")
    waiter.wait(InstanceIds=[instance_id])
    print("Instance is now terminated")
# terminate_instance("i-0f139dc554b1e9210")