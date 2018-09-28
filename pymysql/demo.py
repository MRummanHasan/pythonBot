import pymysql
import random

# connection work
conn = pymysql.connect(host='localhost', user='root', password='', db='doctor')
a = conn.cursor()
# end connection work

print("Hi")
greetings = ['hola', 'hello', 'hi', 'hi!', 'hey!', 'hey', 'salam']
random_greeting = random.choice(greetings)
question = ['How are you?', 'How are you doing?']

goodResponses = ['okay', "i'm fine", 'good', 'fine']
random_response = random.choice(goodResponses)

docTypeQue = ['For what problem you want to see doctor?']
docTypeResp = ['eye', 'nose', 'throat']
docTypeAmbigiousResp = ["don't know", 'no idea', 'just feeling ill']

# working logic
while True:
    userInput = input(">>> ")
    if userInput.lower().strip() in greetings or userInput.lower().strip() in goodResponses:
        if userInput.lower().strip() in greetings:
            print("\n" + random.choice(question))

        elif userInput.lower().strip() in goodResponses:
            
            userInput = input(">>> For what problem you want to see doctor? ")

            if userInput.lower().strip() in docTypeResp:
                print("No problem we shall connect you to " + userInput + " Specialist")
                # execute query
                sql = 'SELECT docName,docType,docTimeFrom,docTimeTo,docDay FROM `timings` WHERE docType = "ENT";'
                a.execute(sql)
                data = a.fetchall()
                # print(data)
                for entry in data:
                    print("Dr. " + str(entry[0]) + "\n " + str(entry[1]) + "\n " + str(
                        entry[2])[-5:] + " to " + str(entry[3]) + "\n " + str(entry[4])+"\n")
                print("Book Your appointment \n BYE Take Care")
                break

            else:
                # General physician query
                sql = 'SELECT docName,docType,docTimeFrom,docTimeTo,docDay FROM `timings` WHERE docType = "General";'
                a.execute(sql)
                data = a.fetchall()
                # print(data)
                for entry in data:
                    print("Dr. " + str(entry[0]) + "\n " + str(entry[1]) + "\n " + str(entry[2])[-5:] + " to " + str(entry[3]) + "\n " + str(entry[4])+"\n")
                break

    
    else:
        print("I did not understand what you said")


# sql = 'SELECT * FROM `timings`;'
# a.execute(sql)
# data = a.fetchall()
# print(data)

# i = 0
# for entry in data:
#     print("Dr. "+ str(entry[0]) +"\n "+ str(entry[1]) +"\n "+ str(entry[2])[-5:] +" to "+ str(entry[3]) +"\n "+ str(entry[4])+"\n")
#     # for e in entry:
#         # print(e)
#         # i = i + 1
