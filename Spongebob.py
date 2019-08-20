while True:
    print(" ")
    print("Plankton: I can't wait to get my hands on the Krabby Patty recipe!")
    print(" ")
    answer = input("Plankton: Can you help me with my quest? (1) Yes or (2) no?")
    print(" ")
    #fix this part
    if answer == "1":
        print("Plankton: Great! Let's go make ourselves some money!!")
    if answer == "2":
        print("Plankton: You Spongebob-loving traitor. You're gonna help me anyway.")
    print(" ")
    choice1 = input("Where should we go first? (1) Seaweed or (2) Coral?")
    print(" ")
    #SEAWEED PATHWAY
    if choice1 == "1":
        print("Hmm... I wonder where it could be.")
        print("What's that in the rustling in the seaweed?")
        print("Holy jellyfish! It's Spongebob's evil sidekick... Gary.")
        choice101 = input("Should I (1) leave or should I (2) stay?")
        #leave, get mermaid hint
        if choice101 == "1":
            print("Let's get out of here!")
            #mermaid hint
            print("Oh, look! There's a mermaid!")
            print("Mermaid: Are you lost?")
            print("Plankton: No, I'm looking for the Krabby Patty recipe. Can you help me?")
            print("Mermaid: Yes, I can give you a hint.")
            print("Mermaid: You will feel blue if you choose the blue.")
            print("Plankton: Thanks for the tip.")
            print("Mermaid: Goodbye and good luck with your quest.")
            print("The mermaid swims away and the mast of an old sunken ship comes into view above the seaweed.")
            choice4044 = input("Plankton: Should I (1) explore the ship or (2) just leave it alone?")

            if choice4044 == "1":
                print("The dilapidated ship is huge with many rooms and passageways.")
                print("The passageways are convoluted and filthy.")
                print("Plankton: I am lost in this ship.")
                choice5055 = input("Plankton: Which way should I go (1) left or (2) right?")

                if choice5055 == "1":
                    print("A monsterous shark swimms down the hallway right into Plankton.")
                    print("Plankton never stood a chance.")
                    print("You die.")
                    break

                if choice5055 == "2":
                    print("This way doesn't lead out of the ship.")
                    print("You get lost. Try again.")
                    continue
            if choice4044 == "2":
                print("A dark cave comes into veiw in the murky water.")
                print("Plankton: I have heard rumers that the Krabby Patty recipe is hidden in a cave like this one.")
                print("Plankton enters the cave and finds two glass bottles with rolled up paper inside them.")
                print("One of the bottles is blue and the other one is green.")
                choice3033 = input("Choose either (1) green or (2) blue.")

                if choice3033 == "2":
                    print("Wrong bottle. Try again.")
                    continue

                if choice3033 == "1":
                    print("Plankton: I found the Krabby Patty recipe!")
                    print("Now I can put the Krusty Krab out of business!")
                    print("Victory is mine! Ha Ha Ha!")
                    break

        #stay
        if choice101 == "2":
            print("You get lost in the kelp.")
            print("Try again.")
            continue

    #CORAL PATHWAY
    if choice1 == "2":
        print("Plankton: Where is it???")
        print("Plankton: AHH Giant pufferfish!!")
        print("Plankton: IT'S AS BIG AS A WHALE.")
        print("Pufferfish: *stares menacingly with its red eyes*")
        choice202 = input("Plankton: Should I (1) retreat or (2) stand my ground?")
        #retreat, died
        if choice202 == "1":
            print("The pufferfish swam you down and impaled you with its spikes.")
            print("You died.")
            break
        #stand ground, stay alive
        if choice202 == "2":
            print("The pufferfish leaves you alone.")
            print("You are still alive.")
            print("An octopus of collosal proporations comes up from behind.")
            print("Plankton: I'm looking for the Krabby Patty recipe. Can you help me?")
            print("Octopus: Yes, I'd love to help you!")
            print("Octopus: The hint is- You will feel blue if you choose the blue.")
            print("Octopus: Would you like to meet the rest of my family?")
            choice2022 = input("(1) Yes, meet the family or (2) No, lets leave.")

        if choice2022 == "1":
            print("Octopus: This is my father Jumbo Kraken.")
            print("An Enormous grey Kraken with leathery tenticles climbs out from behind a coral fan.")
            print("Plankton: What! I thought that was just an old wrinkly washed up barnacle.")
            print("Kraken: How dare you insolent little whippersnapper! I'm gonna kill you!")
            print("You die")
            break

        if choice2022 == "2":
            print("A dark cave comes into veiw in the murky water.")
            print("Plankton: I have heard rumers that the Krabby Patty recipe is hidden in a cave like this one.")
            print("Plankton enters the cave and finds two glass bottles with rolled up paper inside them.")
            print("One of the bottles is blue and the other one is green.")
            choice3033 = input("Choose either (1) green or (2) blue.")

            if choice3033 == "2":
                print("Wrong bottle. Try again.")
                continue

            if choice3033 == "1":
                print("Plankton: I found the Krabby Patty recipe!")
                print("Now I can put the Krusty Krab out of business!")
                print("Victory is mine! Ha Ha Ha!")
                break
