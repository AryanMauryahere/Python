# n = int(input("Enter a number: "))


# product = 1
# for i in range(1 , n+1):
#     product = product * i

    
# print(product)


###FACTORIAL usomg RECURRSION

n = int(input("Enter a number: "))

def factorial(n):
    if (n == 1 or n == 0):
        return 1

    return n* factorial(n-1)

print(factorial(n))

