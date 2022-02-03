import random as r


def user_guess():   #function to take input user's guess
    n=input()
    if(n>='1' and n<='3'):
        return int(n)
    else:
        print("Please pick a number between 1,2,3:  ")
        return user_guess()


def game_desc():     #game description
    print("WELCOME TO GUESS THE POSITION!")
    print("The element is present in one of the positions from 1 to 3 ")
    print("LET'S PLAY!")
    print("Please help me find the correct position of the element...\n So what is your guess ?")


mylist=['','O','']
r.shuffle(mylist)
game_desc()
c=user_guess()
for i in range(3):
    if (mylist[i]!=''):
        store=i+1
if(c==store):
    print("CORRECT GUESS !!")
else:
    print("Wrong! Better luck next time")
    print("The ball was present in {} position".format(store))