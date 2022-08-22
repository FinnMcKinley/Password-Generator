import random # Imports the random library so we can choose suedo random charactors

# Defines Variables
symbolsQuestionDone = 0
generatorStartDone = 0
extraInfoAskDone = 0
password = ""

while generatorStartDone == 0:
    passwordGeneratorStart = str(input(" * Do you need a password? Y/N *\n")).upper()
    if passwordGeneratorStart == "Y":
        
        generatorStartDone = 1
        
        # Defines the random Charactors to use
        lowerAlphabet = "qwertyuiopasdfghjklzxcvbnm"
        upperAlphabet = "QWERRTYUIOPASDFGHJKLZXCVBNM"
        symbols = "!@#$%^&*()"
        numbers = str(1234567890)

        #Asks user how long the password should be
        length = int(input(" * How long would you like your password? *\n"))

        # Asks the user if they want symbols & numbers or just letters
        while symbolsQuestionDone == 0:
            yesSymbols = str(input(" * Do you want symbols & numbers Y/N *\n")).upper()
            
            # Randomizes a letter, symbol and number based password
            if yesSymbols == "Y":
                for x in range(length):
                    keyType = random.randint(0,3)
                    if keyType == 0:
                        randomcharacter = lowerAlphabet[random.randint(0,25)]
                        password += str(randomcharacter)
                    if keyType == 1:
                        randomcharacter = upperAlphabet[random.randint(0,25)]
                        password += str(randomcharacter)
                    if keyType == 2:
                        randomcharacter = symbols[random.randint(0,9)]
                        password += str(randomcharacter)
                    if keyType == 3:
                        randomcharacter = numbers[random.randint(0,9)]
                        password += str(randomcharacter)
                symbolsQuestionDone = 1

            # Randomizes a letter-only password
            elif yesSymbols == "N": 
                for x in range(length):
                    keyType = random.randint(0,1)
                    if keyType == 0:
                     randomcharacter = lowerAlphabet[random.randint(0,25)]
                     password += str(randomcharacter)
                    if keyType == 1:
                        randomcharacter = upperAlphabet[random.randint(0,25)]
                        password += str(randomcharacter)
                symbolsQuestionDone = 1

             # Returns Error
            else:
                print(" * Invalid input *\n")

        # Asks user what the service is
        companyName = str(input(" * What is the name of the service/app? *\n"))

        # Asks user for the username used
        username = str(input(" * What is the username used? *\n"))

        # Asks user for the email used
        email = str(input(" * What is the email used? *\n"))

        # Asks user for any extra information
        while extraInfoAskDone == 0:
            extraInfoAsk = str(input(" * Do you want to add anything else? Y/N *\n")).upper()
            if extraInfoAsk == "Y" or extraInfoAsk == "y":
                extraInfo = str(input(" * What do you want to add? *\n"))
                extraInfoAskDone = 1
            elif extraInfoAsk == "N" or extraInfoAsk == "n":
                extraInfo = ""
                extraInfoAskDone = 1
            else:
                print(" * Invalid input *\n") # Returns Error

        # Writes Information to the Password File
        passwordFile = open("passwords.txt", "a")
        passwordFile.write("\n")
        passwordFile.write(companyName)
        passwordFile.write("\n")
        passwordFile.write(username)
        passwordFile.write("\n")
        passwordFile.write(email)
        passwordFile.write("\n")
        passwordFile.write(str(password))
        passwordFile.write("\n")
        passwordFile.write(extraInfo)

        # Verifies Completion
        print("Awesome! Your login information was saved!")

    elif passwordGeneratorStart == "N":
        
        generatorStartDone = 1

        # Asks user what the service is
        companyName = str(input(" * What is the name of the service/app? *\n"))

        # Asks user for the username used
        username = str(input(" * What is the username used? *\n"))

        # Asks user for the email used
        email = str(input(" * What is the email used? *\n"))

        # Asks user for the password used
        passwordUsed = str(input(" * What is the passsword used? *\n"))

        # Asks user for any extra information
        while extraInfoAskDone == 0:
            extraInfoAsk = str(input(" * Do you want to add anything else? Y/N *\n")).upper()
            if extraInfoAsk == "Y" or extraInfoAsk == "y":
                extraInfo = str(input(" * What do you want to add? *\n"))
                extraInfoAskDone = 1
            elif extraInfoAsk == "N" or extraInfoAsk == "n":
                extraInfo = ""
                extraInfoAskDone = 1
            else:
                print(" * Invalid input *\n") # Returns Error
        
        # Writes Information to the Password File
        passwordFile = open("passwords.txt", "a")
        passwordFile.write("\n")
        passwordFile.write(companyName)
        passwordFile.write("\n")
        passwordFile.write(username)
        passwordFile.write("\n")
        passwordFile.write(email)
        passwordFile.write("\n")
        passwordFile.write(passwordUsed)
        passwordFile.write("\n")
        passwordFile.write(extraInfo)

        # Verifies Completion
        print("Awesome! Your login information was saved!")

    else:
        print(" * Invalid input *\n") # Returns Error
    