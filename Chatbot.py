# Chatbot
#--- Define your functions below! ---
def intro(string):
    print("Hello " + string + "!")
    print("My name is Casper.")
    print("Do you need help?")
    newstring = string
    if len(string) == 5:
        print("hello")
# --- Put your main program below! ---
def main():
    girl = "Ladies"
    guy = "Fellas"
    all = "Y'all"
    intro(girl)
    intro(guy)
    intro(all)
    # runs intro function
    while True:
        answer = input("(What will you say?) ")
        print("That's cool!")

# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main() # calls function
