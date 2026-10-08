a = {

  "key" : "value" ,
  "aryan" : "good",
  "didi" : "bad",
 }

# # print(a.values())
# # print(a["aryan"])
# # print(a.keys())
# # print(a.items())

# a.update({"c" : 3})
# print(a)

# # print(a.pop("c"))
# print(a)

# print(a.popitem())
# print(a)

# a.clear()
# print(a)

a.update({"aryan": "bad"})
print(a)

print(a.get("rohan")) #prints none
# print(a["rohan"]) #returns an error that the only diff in both

### sets

s = set() #an empty set

z = {} #an empty dictionary

set = { 1, 2, 3, 2, 2, 2, 3}
print(set) #repeat nahi hote sets ke andar ke elements
set.remove(3)
print(set) #repeat nahi hote sets ke andar ke elements
# set.clear()
# print(set) #repeat nahi hote sets ke andar ke elements

set2 = {1, 5, 6, 89}

print(set.union(set2))
print(set.intersection(set2))