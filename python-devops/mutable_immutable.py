#Mutable objects can be changed after they are created. Examples include lists, dictionaries, and sets.
#Immutable objects cannot be changed once they are created. Examples include strings, integers, and tuples.

rtr_addr="10.1.1.2"

gate_way=rtr_addr
# print(gate_way)
# print(rtr_addr)

#identify object
rtr_=id(rtr_addr)
print(rtr_)
gat_=id(gate_way)
print(gat_)

#When you change the value of an immutable object, Python creates a new object in memory.
ssh_timeout=20
immutable=id(ssh_timeout)
print(immutable)

#working with lists
data_center=["sf", "la", "den", "dal"]
list_=id(data_center)
print(list_)