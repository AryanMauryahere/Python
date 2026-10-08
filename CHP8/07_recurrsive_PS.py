#Write a recursive function to calculate the sum of first n natural numbers


n = int(input("Enter a number: "))

def sum_of_num(n):  
    if(n == 0):
        return 0  
    return n + sum_of_num(n-1)

print(f"The sum of first n numbers are : {sum_of_num(n)}")
