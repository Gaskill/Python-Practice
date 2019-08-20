# Hangman game
import random
pontentialwords = ["mango", "cranberry", "pomegranate", "pear", "plum", "current", "fig", "guava", "kumquat", "mulberry", "nectarine", "passionfruit", "tangerine", "peach", "apricot", "lime", "lemon", "huckleberry", "grapefruit", "starfruit", "strawberry", "blueberry", "grape", "banana", "papaya", "cantalope", "rasberry", "blackberry", "thimbleberry", "cherry", "kiwi", "pineapple", "watermelon", "dragonfruit", "honeydew", "orange"]
word = random.choice(pontentialwords) #picks random word from list
#print(word)
word = word.lower() #changes to lowercase
attemps = 6
guesses = ''

while attemps > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char,)
        else:
            print("_",)
            failed +=1

    if failed ==0:
        print("You won")
        break

    print()

    guess = input("Guess a letter: ")

    guesses += guess

    if guess not in word:
        print("You have %s guesses left." %(attemps))

        attemps -=1
        print("Wrong")

    if attemps == 0:
        print("You lose")
        print("The word was: " + word)
