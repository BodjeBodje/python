"""
    A UNIQUE COLLECTION OF ELEMENTS
        #id_no
"""

set_=()
# all the members of class24 are unique
class24={"amadou","mohamed","samba","amadou"}
print(type(class24))
print(class24)

# all the members of class24 are unique
class25={"john","doe","jane","john"}
print(type(class25))
print(class25)

print("=====================================================================================")

# what members are both in class24 and class25? Intersection (common area)
intersection=class24 & class25
intersection2=class24.intersection(class25)
print(intersection)

# what members are in class24 and not in class25? Difference 
difference_24_25=class24 - class25
difference_24_25=class24.difference(class25)
print(difference_24_25)

#what members ares in class25 and not in class24? Difference
difference_25_24=class25 - class24
difference_25_24=class25.difference(class24)
print(difference_25_24)

# what members are in class24 or class25? Union
union_24_25=class24 | class25
union_24_25=class24.union(class25)
print(union_24_25)