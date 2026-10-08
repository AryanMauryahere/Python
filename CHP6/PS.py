#Write a program to find the greatest of four numbers entered by the user

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
num4 = float(input("Enter fourth number: "))

if(num1>num2 and num1>num3 and num1> num4):
    print(num1, "is the largest number")

elif(num2>num1 and num2>num3 and num2>num4):
    print(num2, "is the largest number")

elif(num3>num1 and num3>num1 and num3>num4):
    print(num3, "is the largest number")

else:
    print(num4, "is the largest number")
