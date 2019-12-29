#This function is meant to take a message and encrypt it using one-time-message
#The message and key are inputted in the main function
#This function takes the inputs from the main function and encrypts them using one-time-pad. It can also take a message and keystream from the RC4 function and further encrypt it with the same process
#This function is interchangable meaning it can be used to encrypt and decrypt one-time-pad messages
def oneTime(message, key):

    user_input = zip(message, key)
    theMessage = ''.join(chr(ord(msg_letter) ^ ord(key_letter)) for msg_letter, key_letter in user_input)
    return theMessage


#This function is meant to take a message and encrypt it using RC4
#The message and the key are inputted in the main function
#The function takes the inputs from the main function and encrypts them using RC4
#This function is interchangable meaning it can used to encrypt and decrypt RC4 messages
def RC4(message, key):

    #Following lines setup the variables
    keyStream = ""
    S = []
    for x in range(0, 256):
        S.append(x)

    #The following lines are creating a permutation
    j = 0
    for i in range(0, 256):
        j = (j + S[i] + ord(key[i % len(key)])) % 256
        temp = S[i]
        S[i] = S[j]
        S[i] = temp

    #Resetting values to zero for use within the keystream generation
    i = 0
    j = 0
    while len(keyStream) < len(message):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        temp = S[i]
        S[i] = S[j]
        S[j] = temp
        k = S[(S[i] + S[j]) % 256]
        keyStream += chr(k)

    #
    theMessage = oneTime(message, keyStream)
    return theMessage


def main(user_choice=None):

        while user_choice != "3":
            print("""
            --------------------------------------------------------------------------------------------------------------------------------------------------------------
            1- One-Time Pad
            2- RC4
            3- Exit
            --------------------------------------------------------------------------------------------------------------------------------------------------------------""")

            user_choice = input("\nPlease choose from above:\n")
            #initiates the oneTime function
            if user_choice == "1":
                #The following inputs are passed into the oneTime function provided that the conditions for the key are met
                message = input("Write the message you want here:\n")
                key = input("Write the key you want to use here. NOTE make sure that the key matches the length of the message your message is " + str(len(message)) + " characters long:\n")

                #If the key length is not the same as the message length, then the method fails and the user has to start over
                if len(key) != len(message):
                    print(str(len(key)) + " The key is not the same length as the message")
                else:
                    theMessage = oneTime(message, key)
                    print("Encrypted message: " + theMessage)
                    print("Decrypted message: " + oneTime(theMessage, key))

            #Initiates the RC4 function
            elif user_choice == "2":
                #The following inputs are passed into the RC4 function provided that the conditions for the key are met
                message = input("Write the message you want here:\n")
                key = input("Write the key you want to use here. Please use a key at least 1 character long:\n")

                #If the key length is less than 1 (basically if the user doesn't input anything), the method fails and the user has to start over
                if len(key) < 1:
                    print("Please enter a key")
                else:
                    RC4(message, key)
                    theMessage = RC4(message, key)
                    print("Encrypted message: " + theMessage)
                    print("Decrypted message: " + RC4(theMessage, key))

main()