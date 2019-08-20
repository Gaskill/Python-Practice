#Guess the number game

Attempts = 0
from random import * #picks random number from 1 through 20
aRandomNumber = randint(1, 20)
#print(aRandomNumber)
while True:

    Attempts += 1
    #asks for your guess
    guess = input("Guess a number between 1 and 20 (inclusive)")
    if not guess.isnumeric(): #guess a number not a word
        print("Guess a positive whole number")
        Attempts -= 1 #this doesn't count as a guess
        continue
    else:
        guess = int(guess) #covert to integer

    if guess < 1 or guess > 20:
        print("Guess a number between 1 and 20")
        Attempts -= 1 #this doesn't count as a guess
        continue

    if guess == aRandomNumber: #correct
        print("Yay! You guessed the right number!")
        break

    if Attempts == 3: #out of tries
        print("Sorry! You died the number was %s." %(aRandomNumber))
        break

    if  guess > aRandomNumber: #guess lower
        print("The number is lower than %s" %(guess))

    else: #guess < aRandomNumber: #guess higher
        print("The number is higher than %s" %(guess))
