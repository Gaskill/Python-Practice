#Guess the number game

i = 0
from random import * #picks random number from 1 through 20
aRandomNumber = randint(1, 20)
#print(aRandomNumber)
for i in range(3):

    #asks for your guess
    guess = input("Guess a number between 1 and 20 (inclusive)")
        While not guess.isnumeric(): #guess a number not a word
            print("Guess a positive whole number")

    if    guess = int(guess) #covert to integer

    if guess < 1 or guess > 20:
        print("Guess a number between 1 and 20")
        i -= 1 #this doesn't count as a guess
        continue

    if guess == aRandomNumber: #correct
        print("Yay! You guessed the right number!")
        break

    if  guess > aRandomNumber: #guess lower
        print("The number is lower than %s" %(guess))

    else: #guess < aRandomNumber: #guess higher
        print("The number is higher than %s" %(guess))

 #out of tries
print("Sorry! You died the number was %s." %(aRandomNumber))
