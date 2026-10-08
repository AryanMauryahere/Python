"""
1 =  rock
2 = paper
3 = scissors

"""
import random
computer = random.choice([1 , 2 , 3])
computerdict = {1 : "rock" , 2 : "paper" , 3 : "scissors"}
computerstr = computerdict.get(computer)

user = input("Enter your choice: ")
userdict = {"r" : 1 , "p" : 2 , "s" : 3 }
usernum = userdict.get(user)

print(f"The computer chose : {computerstr}\nYou chose : {computerdict.get(usernum)}")



if(computer == usernum):
    print("It's a draw!")

else:
    if(computer == 1 and user == "p"):
        print("You Win!")

    elif(computer == 1 and user == "s"):
        print("You lose!")

    elif(computer == 2 and user == "r"):
        print("You Lose!")

    elif(computer == 2 and user == "s"):
        print("You win!")

    elif(computer == 3 and user == "r"):
        print("You win!")

    elif(computer == 3 and user == "p"):
        print("You Lose!")

    else:
        print("Something went wrong!")



