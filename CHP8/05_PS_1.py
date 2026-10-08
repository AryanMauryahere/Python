#Write a program using functions to find greatest of three numbers.

def greater_num():

    a1 = int(input("Enter 1st number: "))
    a2 = int(input("Enter 2nd number: "))
    a3 = int(input("Enter 3rd number: "))

    if(a1>a2 and a1>a3):
        print(f"{a1} i sthe largest number.")

    elif(a3>a2 and a3>a1):
        print(f"{a3} i sthe largest number.")

    else:
        print(f"{a2} i sthe largest number.")

greater_num()