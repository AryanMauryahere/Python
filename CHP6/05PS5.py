#Write a program which finds out whether a given name is present in a list or not.

names = input("Enter a name: ").lower()

names_lists = ["aryan", "neha", "raj", "sidd"]

if any(name in names for name in names_lists):
    print("The name is there in the list")

else:
    print("The name is not there in the list")

