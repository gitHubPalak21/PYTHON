#list
#lists are mutable
#container to store values
#zero based indexing
#list mai directly changes hote hai ji


friends = ["Apple","Orange",3,4,False,"akash","Yash"]

friends[0]= "palak"
print(friends[0])
print(friends[1:4])
friends.append("palak")
#methods for list

li = [0,4,4,4,4,43,3,2,2,4]
li.sort()
li.reverse()
print(li)
print(sum(li))

#ye khna chahta hai is index pr aajaye 56 hamara uska index hi ye bn jaye
li.insert(6,56)# 6 is the index
#pop method delete at a particular index

value = li.pop(3)
print(value)
print(li)

#input list elements and append them in list

fruits=[]
f1=input("enter fruit1: ")
fruits.append(f1)
f2=input("enter fruits2: ")
fruits.append(f2)




