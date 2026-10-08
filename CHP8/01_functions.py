def avg(avgr, end="Thank you"):
    a = int(input("Enter a number: "))
    c = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    print(avgr , end)
    average = ( a + b + c)/3
    print(average)
    return average
a1 = avg("")
print(a1)

avg("Hello")
avg("Hello")
avg("Hello")
avg("Hello")