'''
Write a python function to print first n lines of the following pattern.

***
**   for n = 3
*

'''

# n = int(input("enter a number: "))
def pattern(n):
    if(n == 0):
        return
    print("*"*n)
    pattern(n-1)

print(pattern(3))

# n = int(input("enter a number: "))
    
# for i in range(n+1):
#     print("*"*(n-i))