#for loop
for i in range(1,6):
    print(i)
#for loops with list
l = [1,4,6,567,4,568]
for i in l:
    print(i)
#for loop with tuples
t= (6,456,345,4)
for i in t:
    print(i)
#for loop with tuples
s="harry"
for i in t:
    print(i)    

#for loop with else statement
l=[9,0,8]
for item in l:
    print(item)
else:
    print("done")    #this is printed when the loop exhausts
#while loop
while(i<5):
    print(8)
    i=i+1

#continue keyword is used to skip a particular index
#break keyword is used to come out of the loop


#print table
n=int(input("enter the table u want ot get printed"))

for i in range(1,11):
    print(f"{n}*{i}={n*i}")

# whether a number is prime or not

n=int(input("enter the number"))

for i in range(2,n):
    if(n%i==0):
        print("number is not prime")
    else:
        print("number is prime")    