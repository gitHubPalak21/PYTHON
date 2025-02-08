#dictionaries are used for the key value pair
#mutable
marks ={
    "palak" :90,
    "harsh":80,
    "bhavu":100,
    list:[4,5]
     }

print(marks["harsh"])

#properties of dictionaries
#it is mutable
#it is indexed
#this is a key value pair thing
print(marks.keys())
print(marks.values())
marks.update({"harry":44,"palak":101,"shaurya":99})
print(marks)

#difference in both is when we will type harsh2
print(marks.get("harsh"))#this will give none or null
##this will put up an error

d={}#empty dictionaries

#question
d={}

name =input("enter the friend name")
lang =input("enter the language name")
d.update({name:lang})
name =input("enter the friend name")
lang =input("enter the language name")
d.update({name:lang})
name =input("enter the friend name")
lang =input("enter the language name")
d.update({name:lang})
name =input("enter the friend name")
lang =input("enter the language name")
d.update({name:lang})
name =input("enter the friend name")
lang =input("enter the language name")
d.update({name:lang})

print(d)













