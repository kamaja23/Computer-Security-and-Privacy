#Utilizes a modified version of the Caesar Cypher to encrypt, decrypt, or break a test
#Encrypt function: Reads from a file 'plaintext.txt', reads the message and prints the ciphertext to another text file called 'ciphertext.txt'
#Decrypt function: Reads from the 'ciphertext.txt' file and prints the file into the terminal
#Break function: Allows the user to determine the key needed in order to decrypt or encrypt the message.

def encrypt(key, message):

    theMessage = ''.join(chr(ord(letter) + int(key)) for letter in message)
    file = open('ciphertext.txt', 'w')
    file.write(theMessage)
    print(theMessage)


def decrypt(key, message):

    theMessage = ''.join(chr(ord(letter) - int(key)) for letter in message)
    print(theMessage)


def Break(message):

    key = 0
    correctCharacter = False
    while (key < 26) or not (correctCharacter != True):
        key += 1
        theMessage = ''.join(chr(ord(letter) - int(key)) for letter in message)
        print(theMessage + ' key: ' + str(key))
        userInput = input("Please verify this message is correct\n")
        if userInput.lower() == "y":
            correctCharacter = True
        else:
            correctCharacter = False


def main(choice=None):

    global target
    while choice != 4:
        print(
            "1- Encrypt\n"
            "2- Decrypt\n"
            "3- Break\n"
            "4- Exit\n"
        )
        choice = int(input("Choose from the above choices:\n"))

        if choice == 1:
            try:
                target = open('plaintext.txt', 'r')
            except:
                print(
                    "The text file 'plaintext.txt' does not appear to exist. Ensure that the file is in the proper directory")
            contents = target.read()
            key = int(input(
                "This program is using Caesar's Cipher. Please specify how much you want to shift the characters:\n"))
            encrypt(key, contents)

        elif choice == 2:
            try:
                target = open('ciphertext.txt', 'r')
            except:
                print(
                    "The text file 'ciphertext.txt' does not appear to exist. Ensure that the file is in the proper directory")
            contents = target.read()
            key = int(input("Please input the key below\n"))
            decrypt(key, contents)

        elif choice == 3:
            try:
                target = open('ciphertext.txt', 'r')
            except:
                print(
                    "The text file 'ciphertext.txt' does not appear to exist. Ensure that the file is in the proper directory")
            contents = target.read()
            Break(contents)

        else:
            print("Error. Input out of range\n")

    print("\nGoodbye")


main()