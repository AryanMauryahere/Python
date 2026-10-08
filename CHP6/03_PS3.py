# A spam comment is defined as a text containing following keywords: “Make a lot of
# money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.


# cmt = input("Enter a comment: ")
# cmt_lwr = cmt.lower()

# if(cmt == "click this"):
#     print("It is a spam comment.")    

# elif(cmt == "subscribe this"):
#     print("It is a spam comment.")

# elif(cmt == "but now"):
#     print("It is a spam comment.")

# else:
#     print ("Thank you fo rthe comment.")



### USING LISTS

# 1. Store your keywords in a list
# spam_keywords = [
#     "make a lot of money", 
#     "buy now", 
#     "subscribe this", 
#     "click this"
# ]

# # 2. Get the comment
# comment = input("Enter your comment: ").lower()

# # 3. Check against the list
# # any() returns True if at least one of the conditions inside is True
# if any(keyword in comment for keyword in spam_keywords):
#     print("Warning: This comment is Spam.")
# else:
#     print("This comment is Not Spam.")


c1 = "make a lot of money"
c2 = "buy now"

c = input("Add a comment: /")

if(c1 in c or c2 in c):
    print("this ia a spam comment")

else:
    print("This is not a spam comment")