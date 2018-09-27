import pymysql
import random

# connection work
conn = pymysql.connect(host='localhost', user='root', password='', db='doctor')
a = conn.cursor()
# end connection work

print("Hi")
greetings = ['hola', 'hello', 'hi', 'Hi', 'hey!', 'hey']
random_greeting = random.choice(greetings)
question = ['How are you?', 'How are you doing?']

goodResponses = ['okay', "I'm fine", 'good']
random_response = random.choice(goodResponses)

docTypeQue = ['For what problem you want to see doctor?']
docTypeResp = ['Eye', 'Nose', 'Throut']
docTypeAmbigiousResp = ["Don't know", 'No idea', 'Just feeling ill']

# working logic
while True:
    userInput = input(">>> ")
    if userInput in greetings:
        print(random_greeting + "\n " + random.choice(question))
    elif userInput in goodResponses:
        print("For what problem you want to see doctor? ")
    elif userInput in docTypeResp:
        print("No problem we shall connect you to " + userInput + " Specialist")
        if userInput in docTypeResp:
            # execute query
            sql = 'SELECT * FROM `timings` WHERE docType = "ENT";'
            a.execute(sql)
            data = a.fetchone()
            print(data)
        else:
            # General physician query
            sql = 'SELECT * FROM `timings` WHERE docType = "General";'
            a.execute(sql)
            data = a.fetchmany()
            print(data)

    elif userInput in docTypeAmbigiousResp:
        print("Sorry about that... \n No problem we shall connect you to the Doctor")
        # query for physician
    else:
        print("I did not understand what you said")


# sql = 'SELECT * FROM `timings`;'
# a.execute(sql)
# countrow = a.execute(sql)

# print("Number of rows: ", countrow)
# data = a.fetchone()

# print(data)
