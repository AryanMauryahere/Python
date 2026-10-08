#Write a program to find whether a given username contains less than 10 characters or not
char = input("Enter a character: ").lower()

if(len(char)< 10):
    print("The character has less than 10 character")

else:
    print("The character is larger that 10 character")