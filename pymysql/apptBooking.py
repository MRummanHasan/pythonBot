# import pymysql
import random

# Install WAMPs/XAMP, make localhost
# # connection work
# conn = pymysql.connect(host='localhost', user='root', password='', db='HealthSystem')
# a = conn.cursor()
# # end connection work

# # FETCH PATIENT DATA
# filepath = 'patientDetail.txt'
# listp = []
# # Data Fetching from Txt File
# with open(filepath) as fp:
#     line = fp.readline()
#     while line:
#         l = line.split(',')
#         line = fp.readline()
#         listp.append(l)

docfilepath = 'docDetail.txt'
list = []
# Data Fetching from Txt File of DOCTOR
with open(docfilepath) as fp:
    line = fp.readline()
    while line:
        l = line.split(',')
        line = fp.readline()
        list.append(l)

for docData in list:
    print(docData)
# print("Hi")

greetings = ['hola', 'hello', 'hi', 'hi!', 'hey!', 'hey', 'salam']
random_greeting = random.choice(greetings)

BOTGreeting = [
    'Welcome. I can schedule your appt?', 'How are you doing? I can schedule your appointment']

docTypeQue = ['For what problem you want to see doctor?']
docTypeResp = ['eye', 'nose', 'throat']

fallbackIntent = ['I didnot get that. Can you repeat?',   'I didnot get that. Can you say it again?',
                  'I missed that, say that again?', 'Sorry, can you say that again?']


# input userInput and Intents
# Function: check entitites (find similar word in sentence)
# putput: True/False
def isContain(userinput, intent):
    userVal = userInput.split(' ')
    for i in userVal:
        if i in greetings:
            print(i)
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
        print("No problem. We shall connect you to " +  userInput + " Specialist\n")
        # execute query
        # sql = 'SELECT docName,docType,docTimeFrom,docTimeTo,docDay FROM `DoctorTimings` WHERE docType = "ENT";'
        # a.execute(sql)
        # pData = a.fetchall()
        for entry in list:
            try:
                if 'ENT' == entry[2]:
                    print("Dr. " + str(entry[1]) + "\n " + str(entry[2]) + "")
                    print("Book Your appointment \n")

                    apptConfirm = True
                    while apptConfirm:
                        apptBooking = input(
                            "Please respond with ('y' or 'n') \n")
                        if apptBooking == 'y':
                            i = 0
                            for entry in list:
                                i = i + 1
                                if 'A' == entry[i]:
                                    entry[i] = "Patient Name"
                                    print("Appt success")
                                    apptConfirm = False
                        elif apptBooking == 'n':
                            print("Bye, see you next soon...!")
                            apptConfirm = False
            except:
                pass

        with open(docfilepath, 'r+') as fp:
            for p in list:
                fp.writelines(entry[0]+","+entry[1]+","+entry[2]+","+entry[3]+","+entry[4] +
                              ","+entry[5]+","+entry[6]+","+entry[7]+","+entry[8]+","+entry[9]+"")
                print(entry[0]+","+entry[1]+","+entry[2]+","+entry[3]+","+entry[4] +
                              ","+entry[5]+","+entry[6]+","+entry[7]+","+entry[8]+","+entry[9]+"")


    else:
        # General physician query
        # sql = 'SELECT docName,docType,docTimeFrom,docTimeTo,docDay FROM `DoctorTimings` WHERE docType = "General";'
        # a.execute(sql)
        # docDataa = a.fetchall()
        for docEntry in list:
            if 'General' in docEntry[2]:
                print("Dr. " + str(docEntry[0]) + "\n " + str(docEntry[1]) + "\n ")
                print("Book Your appointment \n BYE Take Care")

                while True:
                    apptBooking = input("Please respond with ('y' or 'n') \n")

                    i = 4
                    for entry in list:
                        i = i + 1
                        if 'A' == docEntry[i]:
                            docEntry[i] = "Patient Name"
                            break
    print("\n"+random.choice(fallbackIntent))


# Happy Time with BOT
