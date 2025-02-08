#tuple is immutable
#its original thing cannot be changed
#empty tuple
a=()
#tuple with one element
a=(8,4,5,4,3,3,2,5,"palak")
print(type(a))
#a[0]=89 #cannot be changed

#how to count occurence of element
no=a.count(4)
print(no)

#to find index where it is present
i= a.index("palak")

#to find whether this thing is present in my tuple or not

#my_tuple = {8,9,7}
#print(9 in my_tuple)
#it will return the answer in true or false

#for adding we use append
fruits=[]
f1= input("enter the fruit name")
fruits.append(f1)


