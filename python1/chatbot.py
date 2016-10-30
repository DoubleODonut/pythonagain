import wikipedia
import random


text_file = open ("stopwords.txt", "r")
stopwords = text_file.read().split('\n')
text_file.close()

text_file = open ("good.txt", "r")
goodanswers = text_file.read().split('\n')
text_file.close()

text_file = open ("bad.txt", "r")
badanswers = text_file.read().split('\n')
text_file.close()
    

greetings = ["Hi", "Hello", "Hiya <3", "Hey", "Greetings", "Good day"]
randomgreeting = random.choice(greetings)



questions = ["How are you", "Are you Okay", "Are you feeling Okay?"]
randomquestion = random.choice(questions)


        
response = raw_input("What is your name? ")

words = response.split(" ")
for word in words:
    if word not in stopwords:
        print(randomgreeting + " " + word)
        name = word
        
questionanswer = raw_input(randomquestion +"? " )

questionwords = questionanswer.split(" ")
for word in questionwords:
    if word in goodanswers:print("That is good to hear! " + name)
    if word in badanswers: print("Oh dear, I hope you get better. " + name)
while True:
    userSuggests = raw_input("Would you like to ask me something? ")
    finalWord = userSuggests.split(' ', -1)[-1]
    wikipediaAnswer = (wikipedia.summary(finalWord, sentences=1))
    print("Oh, do you mean " + wikipediaAnswer)
