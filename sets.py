s={1,2,3}
#empty set
e=set()#dont use s={ for making emoty set}
m={5,4,4,4,4,4,6,7}
#it will not print the repeating elements

print(m)
print(m,type(m))
#to add in a set 
m.add(3)
#properties of a set
#it is unindexed
#it is unordered
#there is no way to change items in a set
#sets cannot contain duplicate values

#to remove
m.remove(4)
print(m)
#to remove random element
m.pop()
#to clear all the elements in a set
m.clear()

#union
s1={1,45,6}
s2={7,8,1,78}

print(s1.union(s2))
print(s2.intersection(s2))
