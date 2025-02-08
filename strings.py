#string is immutable
#main string nhi change hongi
#ek copy m changes honge

#how to slice a string
name ="harry"
nameshort = name[0:3]#starts from zero but 3 index is not included in this
print(nameshort)

#negative slicing
print(name[-4:-1])
print(name[-4:-1])
print(name[:-1])

# jumped slicing
print(name[0:3:2])

#length of a string
print(len(name))
print(name.endswith("rry"))
print(name.startswith("ha"))
#only the first character capital
print(name.capitalize())

#escape sequence charac
# \n,\t,\',\\

name =input("enter your name: ")

print(f"good safternoon , {name}")
#how to replace in a string
letter = '''hlo i am
palak'''
print(letter.replace("palak","bhavninder").replace("hlo","moshi moshi"))

#how to detect double space in it
#how to find anything in a string using find function it gives the index when it first time occurs
name = "harry is a good boy"
print(name.find(" "))




