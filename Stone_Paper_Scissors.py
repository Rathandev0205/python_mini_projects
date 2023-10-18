import random
list=["rock","paper","scissor"]
computer_wins=0
user_wins=0
while True:
    user_pick=input("rock/paper or scissor: ").lower()
    computer_pick=random.choice(list)
    print("you picked: ",user_pick)
    print("computer picked:",computer_pick)
    if user_pick== "rock" and computer_pick=="scissor":
        print("You won! ")
        user_wins+=1
    elif user_pick== "paper" and computer_pick=="rock":
        print("You won! ")
        user_wins += 1
    elif user_pick== "scissor" and computer_pick=="paper":
        print("you won! ")
        user_wins += 1
    else:
        print("You lost! ")
        computer_wins += 1
        break
print("You win",user_wins,"times.")
print("computer win",computer_wins,"times.")
