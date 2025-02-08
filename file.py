f =open("file.txt")
data = f.read()
lines = f.readlines()
print(data)
print(lines,type(lines))
f.close() 

#how to append in a file

st ="hey harry you are amazing"
f =open("file.txt","a")
f.write(st)
f.close()

#the same work can be done where we don't need to close the file

with open("file.txt") as f:
    print(f.read())

#you don't have to explicitly close the file
