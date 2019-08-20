#find your spirit animal
animals = ["Horse", "Pig", "Kangaroo", "Whale", "Pony", "Lobster", "Chicken", "Seahorse", "Wolf", "Bat", "Tiger", "Lion", "Pufferfish", "Swan", "Bear", "Pigeon", "Salamander", "Iguana", "Lizard", "Bee", "Crow", "Beetle", "Ant", "Elk", "Deer", "Jellyfish", "Fly", "Parrot", "Hamster", "Cow"]
print("Find your spirit animal!")
print(len(animals)) #prints number of animals in list
choice = input("Pick a number 1 though 30.") #gathers player's input
choice_int = int(choice)-1 #matches the number picked with an index from the list
print(choice) #prints the number they chose
print("Your spirit animal is a(n) %s!" %(animals[choice_int]))
