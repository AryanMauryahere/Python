f = open("CHP 9/file.txt" , "a")

f.write("\n2")
f.close()


f = open("CHP 9/file.txt" , "r")

r = f.read()
print(r.lower())
f.close()











