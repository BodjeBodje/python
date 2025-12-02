#initialize a tuple
"""

"""
#using a function
names=tuple()

#use brackets (notation)
names=("John","Doe","Jane","Smith","Emily")

print(names)

#operations that can be performed on tuples

#indexing
elem1=names[1]

#slice a tuple
block_elem=names[1:4]

#============================================inheritance=========================================
#retrieve the count of an element in a tuple
print(names.count("Jane"))

#use cases.
ip_addresses=("192.168.1.1","192.168.1.2","192.168.1.3")

#unpacking tuples
ip1,ip2,ip3=ip_addresses
print(ip1,ip2,ip3)

#casting a list to a tuple
list1=["apple","banana","cherry"]
tuple_from_list=tuple(list1)
print(tuple_from_list)
print(type(tuple_from_list))

# a tuple to a list <-> tuple()
tuple1=("red","green","blue")
list_from_tuple=list(tuple1)
print(list_from_tuple)
print(type(list_from_tuple))

#a string to a tuple <-> tuple()
string1="hello"
tuple_from_string=tuple(string1)
print(tuple_from_string)
print(type(tuple_from_string))