#Opens a file. You can now look at each line in the file individually with a statement like "for line in f:
f = open("dictionary.txt","r") #open is a pre defined function
bad = False #sets bad to false
print("Can your password survive a dictionary attack?")

#Take input from the keyboard, storing in the variable test_password
test_password = input("Type in a trial password: ") #test_password is the user's input
test_password = test_password.lower() #changes passcode to lower case

#Write logic to see if the password is in the dictionary file below here: (use conditionals)
for line in f: #f is the opened dictionary file
    if line.strip() == test_password.strip(): #if a line in the dictionary is the same as the test password
        print("We know your password.")
        print("Your password is %s." %(test_password))
        print("Your password sucks.")
        print("Get a new password.")
        bad = True #sets bad to true so that the other part is not printed
        break #stops the program

if bad == False: #if bad never go changed to True
    print("Your passcode is ok.")
    print("We couldn't guess your passcode.")
