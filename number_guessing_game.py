import random
import math
print("\t Welcome to Number Guessing Game")
print("--------------------------------------------------------")
lower=int(input("Enter Lower Bound :"))
uper=int(input("Enter Uper Bound :"))
x=random.randint(lower,uper)
no=round(math.log(uper-lower + 1,2))
print("You have a",no,"Chanse to guess number")
count=0
while count < no:
    count+=1
    guess=int(input("Enter  Your Guess : "))
    if guess==x:
        print("Congrutulation You Guess No in",count,"tyr")
        break
    elif x>guess:
        print("Guess Number is Small")
    elif x<guess:
        print("Guess Number is High")


if count>no:
    print("Better Luck Next time !!")
else:
    print("The Guess Number is :",x)