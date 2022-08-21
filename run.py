import random # Imports the random library so we can choose suedo random charactors

counter = 0
symbolsQuestionDone = 0

#Asks user how long the password should be
lengthString = input(" * How long would you like your password? * \n")
length = int(lengthString)

# Asks the user if they want symbols & numbers or just letters
while symbolsQuestionDone == 0:
    yesSymbols = str(input(" * Do you want symbols & numbers Y/N *\n"))
    if yesSymbols == "Y":
        symbolsQuestionDone = 1
    elif yesSymbols == "N":
        symbolsQuestionDone = 1
    else:
        print("Not a Valid Answer!")

# Defines the random Charactors to use
lowerAlphabet = "qwertyuiopasdfghjklzxcvbnm"
upperAlphabet = "QWERRTYUIOPASDFGHJKLZXCVBNM"
symbols = "!@#$%^&*()"
numbers = str(1234567890)

# Defines Variable that will include the final password
password = " * Your Password is: "

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

# Randomizes a letter-only password
if yesSymbols == "N": 
    for x in range(length):
        keyType = random.randint(0,1)
        if keyType == 0:
            randomcharacter = lowerAlphabet[random.randint(0,25)]
            password += str(randomcharacter)
        if keyType == 1:
            randomcharacter = upperAlphabet[random.randint(0,25)]
            password += str(randomcharacter)

print(password) # Prints Final Result