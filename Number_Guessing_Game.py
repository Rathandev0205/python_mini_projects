import random
print("Number Guessing Game")
upto=int(input("Enter the no. which you want to make a guess upto: "))
if upto<=0:
    print("Enter the number greater than 0.")
random_number=random.randrange(1,upto+1)
guesses=0
while True:
    guesses+=1
    guess=int(input("Guess the number: "))
    if guess==random_number:
        print("You guessed it Right!")
        break
    else:
        print("Better Luck Next Time.")
        continue

print("you got it correct after ",guesses,"guesses")

