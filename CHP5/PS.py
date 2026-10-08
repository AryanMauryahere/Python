# dict = {
#     "kela" : "Banana",
#     "santra" : "orange",
#     "jamun" : "grapes"
# }
# print(dict.keys())

# word = input("Enter a word u want meaning of:")
# print("the translation of that word is:" ,dict[word])

# #Write a program to input eight numbers from the user and display all the unique numberr once

# s = set()

# number1 = input("Enter 1st number:")
# number2 = input("Enter 2nd number:")
# number3 = input("Enter 3rd number:")
# number4 = input("Enter 4th number:")
# number5 = input("Enter 5th number:")
# number6 = input("Enter 6th number:")
# number7 = input("Enter 7th number:")
# number8 = input("Enter 8th number:")

s.add(int(number1))
s.add(int(number2))
s.add(int(number3))
s.add(int(number4))
s.add(int(number5))
s.add(int(number6))
s.add(int(number7))
s.add(int(number8))

# s.update(number1, number2, number3, number4, number5, number6, number7, number8)


#Can we have a set with 18 (int) and '18' (str) as a value in it?


# s = { 18 , "18"}
# print(s)

# #What will be the length of following set s:
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') # length of s after these operations?

# print(len(s))




#Create an empty dictionary. Allow 4 friends to enter their favorite language as value and
# use key as their names. Assume that the names are unique.

names = {}
a1 = input("Enter your name: ")
a = input("Enter your fav language: ")

b1 = input("Enter your name: ")
b = input("Enter your fav language: ")
c1 = input("Enter your name: ")
c = input("Enter your fav language: ")
d1 = input("Enter your name: ")
d = input("Enter your fav language: ")

names.update({a1 : a})
names.update({b1 : b})
names.update({c1 : c})
names.update({d1 : d})
print(names)

# 7. If the names of 2 friends are same; what will happen to the program in problem 6? ONLY THE FIRST NAME WILL BE PRINTED (SAME NAME)
# 8. If languages of two friends are same; what will happen to the program in problem 6? NO PROBLEM
