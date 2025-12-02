"""_summary_
    man - > {name: "amadou", age: 30, country: "Senegal"}
    
    attributes -> keys
    values -> values of attributes
    
student - > {name:"", age: 25, grade:  "A" }

student["name"] -> "amadou"
    student["age"] -> 25
    student["grade"] -> "A"  
    
ec2 :
    name: "web-server"
    public_ip: "192.168.1.1"
    private_ip: "10.0.0.1"
    key_name: "my-key-pair"
    dns_name: "ec2-192-168-1-1.compute-1.amazonaws.com"
    security_groups: ["sg-12345678", "sg-87654321"]
    tags:list
    
"""
ec2={
    "name":"class24-instance",
    "public_ip":"192.168.1.1",
    "private_ip":"10.0.0.1",
    "key_name":"my-key-pair",
    "dns_name":"ec2-192-168-1-1.compute-1.amazonaws.com",
    "security_groups":["sg-12345678", "sg-87654321"],
    "tags":["tag1","tag2","tag3"]
    }

#operations.

#accessing keys
print(ec2["name"])
print(ec2.get("name"))

#passing values
ec2["name"]="new_name"
print(ec2["name"])

#add more fields
ec2["vpc"]="new_vpc"
print(ec2)

print(ec2.keys())
ec2.pop("vpc")
print(ec2.keys())

for element in ec2.get("tags"):
    print(element) #prints keys
    

print ("=========================================")
my_dict={
    "retr1":"10.100.1.2",
    "retr2":"10.100.2.1",
    "retr3":"10.100.3.1"
}

alt_dict=dict(
    retr1="10.100.1.2",
    retr2="10.100.2.1",
    retr3="10.100.3.1"
)
print(alt_dict)

value=alt_dict["retr1"]
print(value)

value1=alt_dict.get("retr2")
print(value1)

# Assigning a new IP address to the key "rtr1"
my_dict["retr1"]="10.100.4.1"
value2=my_dict["retr1"]
print(value2)

#adding a new key-value pair
my_dict["retr4"]="10.100.5.1"
new_key_value=my_dict["retr4"]
print(new_key_value)

#updating a new key value pair
my_dict["retr1"]="10.100.10.1"
updating=my_dict["retr1"]
print(updating)

#deleting a key value pair
del my_dict["retr1"]
print(my_dict)

#keys(), values(), and items()
all_keys=my_dict.keys()
print(all_keys)
all_values=my_dict.values()
print(all_values)
all_items=my_dict.items()
print(all_items)

#pop method, remove 
pop_=my_dict.pop("retr2")
print(my_dict)

#Dictionary iteration techniques
for k in my_dict:
    print(k)

for k1 in my_dict.values():
    print(k1)

for k2, v in my_dict.items():
    print(k2, v)
    
#Dictionary of dictionary
my_devices={
    'retr1':{
        'host':'device1',
        'device_type':'cisco',
    },
    'retr2':{
        'host':'device2',
        'device_type':'fortinet',
    }
}
print(my_devices)

#dictionary containing lists, Here, ‘routers’ and ‘switches’ have lists of IP addresses.
sf={
    'router':['192.168.1.1', '192.168.2.1'],
    'switches':['192.168.1.20', '192.168.1.30']
}
print(sf)