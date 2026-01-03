import boto3

lightsail = boto3.client("lightsail")

response = lightsail.get_instances()
#print (f"{response}")      #all details
for instance in response["instances"]:
    name = instance["name"]
    state = instance["state"]["name"]
    blueprint = instance["blueprintName"]

    print(f"Name: {name} | State: {state} | OS: {blueprint}")
