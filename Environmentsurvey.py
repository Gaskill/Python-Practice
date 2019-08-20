#Survey Environment

responses = [] #values
questions = [
"Who should be responsible for recycling plastic waste? (1)Government (2)Consumer (3)Manufacturer (4)Independent Business (5)All of the above",
"How much of a problem is global warming to you? (1)Not a problem (2)Small problem (3)Medium problem (4)Big problem (5)The biggest problem",
"What is the most challanging part about being environmentally friendly? (1)Lack of knowlage (2)Inconvenince (3)Cost",
"Do you compost and/or recycle? (1)No (2)When I can (3)All the time",
"What do you think is the largest contributer to carbon emmissions? (1)Transportation/vehicles (2)Agriculture (3)Heat/Electricity (4)Industry (5)Buildings",
"Do you drink bottled water? (1)Everyday (2)occasionally (3)When it is the only option"]

keys = ["responsible", "problem", "challange", "recycle", "contributer"]
list_of_answers = []
done = "NO"
while done == "NO":
    survey_answers = {} #empty dictionary
    print("New survey entry! PLease answer the questions below.")

    for x in range(len(questions)):
        responses = input(questions[x] + ": ")
        survey_answers[keys[x]] = responses
        #print(survey_answers) #answers from one participent

    list_of_answers.append(survey_answers)
    done = input("Are you done taking the survey? Type YES or NO.").upper()

print(list_of_answers) #answers from all survey participents
f = open("answers.json", "r") #r means read it doesn't allow you to edit the data
oldData = json.load(f)
list_of_answers.extend(oldData)
f.close()

f = open("answers.json", "w") #w means write
f.write("\n")
index = 0
for t in list_of_answers:
    if(index < len(list_of_answers)-1):
        json.dump(t, f)
        f.write(",\n")
    else:
        json.dump(t, f)
        f.write("\n")
    index += 1
#for i in range(len(list_of_answers)):
#    responsible = []
#    responsible.append(list_of_answers[i]["responsible"])
#    print(responsible)

import json
with open("answers.json", "a") as f: #open answers as a json file
    f.write("[")
    index = 0 #create a new variable
    for t in list_of_answers:
            if(index < len(list_of_answers)-1):
                json.dump(t, f) #puts information into file
                f.write(",\n") #\n skips a line
            else:
                json.dump(t, f)
                f.write("\n") #no comma means that this is the last json object
            index += 1 #adds 1 to index so that the else statement is eventually reached

with open("answers.json", "a") as f: #opens json file and appends data to it
#open as f means to open it as a file
    f.write("]")
