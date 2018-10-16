import pymysql
import random

# Install WAMPs/XAMP, make localhost
# connection work
conn = pymysql.connect(host='localhost', user='root',
                       password='', db='HealthSystem')
a = conn.cursor()
# end connection work

greetings = ['hola', 'hello', 'hi', 'hi!', 'hey!', 'hey', 'salam']
random_greeting = random.choice(greetings)

BOTGreeting = [
    'Welcome. I can schedule your appt?', 'How are you doing? I can schedule your appointment']

docTypeResp = ['eye', 'nose', 'throat']

fallbackIntent = ['I didnot get that. Can you repeat?',  'I didnot get that. Can you say it again?',
                  'I missed that, say that again?', 'Sorry, can you say that again?']


# Input userInput and Intents
# Function: check entitites (find similar word in sentence)
# putput: True/False
def isContain(userinput, intent):
    userVal = userInput.split(' ')
    for i in userVal:
        if i in greetings:
            return True
        else:
            return False


# working logic
while True:
    userInput = input(">>> ")
    if (userInput.lower().strip() in greetings) or (isContain(userInput, greetings)):
        print("\n" + random.choice(BOTGreeting))

    userInput = input(">>> For what problem you want to see doctor? ")

    if userInput.lower().strip() in docTypeResp or isContain(userInput, docTypeResp):
        print("No problem we shall connect you to " + userInput + " Specialist")
        # execute query
        sql = 'SELECT docName,docType,docTimeFrom,docTimeTo,docDay FROM `DoctorTimings` WHERE docType = "ENT";'
        a.execute(sql)
        data = a.fetchall()
        for entry in data:
            print("Dr. " + str(entry[0]) + "\n " + str(entry[1]) + "\n " + str(
                entry[2])[-5:] + " to " + str(entry[3]) + "\n " + str(entry[4])+"\n")
        print("Vist hospital to see the doctor. \n Bye Take Care")
        break

    else:
        print("\n"+random.choice(fallbackIntent))

# Happy Time with Bot
