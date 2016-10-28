import twitter
import urllib2
import sqlite3
import time

while True:
    console = sqlite3.connect("/Users/gkauri/Library/Application Support/Google/Chrome/Default/History")
    cursor = console.cursor()

    cursor.execute("SELECT urls.title FROM urls")
    rows = cursor.fetchall()

    history = [] #array for storing history

    for row in rows:
        history.append(row) #adds info from row into "history array^"
    
    lastTitle = str(history[-1]) #gets the last item from history and converts it into a string
    title = lastTitle[3:-3] #gets specific information from the row
    print(title) #prints title into terminal
    console.close

    #Load in my keys and secrets from the credentials file into a list (array)
    file = open("TwitterCredentials.txt")
    creds = file.read().split('\n')

    #Create a new API wrapper, passing in my credentials one at a time
    api = twitter.Api(creds[0],creds[1],creds[2],creds[3])

    #Post status update and get the response from Twitter
    response = api.PostUpdate("My last viewed page was: " + title)

    #Print out response text (should be the status update if everything worked)
    print("My last viewed page was: " + title)
    time.sleep(3600)