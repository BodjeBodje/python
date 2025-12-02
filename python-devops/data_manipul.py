squares=[x**3 for x in range(1,7)]
print(squares)

eve_numbers=[x for x in range(1,5) if x%2==0]
print(eve_numbers)

network_devices=[
    "Router1: AA:BB:CC:DD:EE:FF",
    "Switch1: 11:22:33:44:55:66",
    "Firewall1: 99:88:77:66:55:44",
]
mac_address=[device.split(":")[1] for device in network_devices]
print(network_devices)

#Example: Selecting Active Network Devices

network_devices1=[
    {"name":"router", "status":"active"},
    {"name":"switche", "status":"inactive"},
    {"name":"firewall", "status":"active"},
]
active_status=[active for active in network_devices1 if active["status"]=="inactive"]
print(active_status)

acl_rules = [
    {"source": "192.168.1.0/24", "destination": "10.0.0.0/24", "action": "permit"},
    {"source": "10.1.1.0/24", "destination": "192.168.2.0/24", "action": "deny"},
    # More ACL rules...
]

acl_configurations = [
    f"access-list {index} {rule['action']} {rule['source']} {rule['destination']}"
    for index, rule in enumerate(acl_rules, start=100)
]
print(acl_configurations)