a=int(input("enter your age"))

if(a>18):
    print("you are above the age of consent")
    print("good for you")
elif(a<0):
    print("you are entering invalid age")    
else:
    print("you are below age of consent")

print("end of program")

#logical opertors
#we write and or not

# in keyword
p1 = "make in money"
p2= "hlo"
p3="palak"
m= "hlo palak"
if((p1 in m) or(p2 in m) or(p3 in m)):
    print("message is a spam")
    



