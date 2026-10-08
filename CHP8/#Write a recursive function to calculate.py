#Write a recursive function to calculate the sum of first n natural numbers


# n = int(input("Enter a number: "))
# def sum_of_nums(n):
#     if (n == 0):
#         return 0
#     return n + sum_of_nums(n-1)

# print(sum_of_nums(n))


def pattern(n):
    for i in range(0,n+1):
        print("*"*(n-i))

pattern(4)