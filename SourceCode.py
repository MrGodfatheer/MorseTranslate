# Python program to implement Morse Code Encryption and Decryption

'''

VARIABLE KEY
'cipher' -> 'stores the morse translated form of the English string' 
'decipher' -> 'stores the English translated form of the morse string' 
'citext' -> 'stores morse code of a single character'
'i' -> 'keeps count of the spaces between morse characters' 
'message' -> 'stores the string to be encoded or decoded' 

'''

# Dictionary representing the morse code chart 

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
'C': '-.-.', 'D': '-..', 'E': '.',
'F': '..-.', 'G': '--.', 'H': '....',
'I': '..', 'J': '.---', 'K': '-.-',
'L': '.-..', 'M': '--', 'N': '-.',
'O': '---', 'P': '.--.', 'Q': '--.-',
'R': '.-.', 'S': '...', 'T': '-',
'U': '..-', 'V': '...-', 'W': '.--',
'X': '-..-', 'Y': '-.--', 'Z': '--..',
'1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', 
'6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', 
', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', 
'(': '-.--.', ')': '-.--.-'}

# Function to encrypt the string according to the morse code chart 

def encrypt(message):
        cipher = ''
        for letter in message:
                if letter != ' ':                
                        # Looks up the dictionary and adds the # correspponding morse code along with a space to separate morse codes for different characters 
                        cipher += MORSE_CODE_DICT[letter] + ' '
                
                else:
                        # 1 space indicates different characters and 2 indicates different words 
                        cipher += ' '
        print("Your message has been encrypted.")
        return cipher

# Function to decrypt the string # from morse to english

def decrypt(message):
        if ("." or "-") not in message:
                print("Improper input. Retry")
        else:
                # extra space added at the end to access the # last morse code
                message += ' '
                decipher = ''
                citext = ''
                for letter in message:
                        if (letter != ' '):
                                i=0     # counter to keep track of space                                
                                citext += letter        # storing morse code of a single character in case of space                                
                        else:                               
                                # if i = 1 that indicates a new character 
                                # if i = 2 that indicates a new word                                
                                i += 1
                                if i == 2:
                                        decipher += ' '         # adding space to separate words
                                else:
                                        # accessing the keys using their values
                                        decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                                        citext = ""
                print("Your message has been decrypted.")
                return decipher

def reAsk():
        ask = input("\nDo you want to continue again? (y/n): ") 
        if ask == "y":
                menu()
        elif ask == "n":
                print("Thank you & a good day!")
        else:
                print("That's an oops. Try again by giving a valid input.\n")
                reAsk()

def menu():
        print("\nWelcome To EncryptDecrypt")
        print("Select A Facility\n1.Encrypt A Sentence\n2.Decrypt Morse") 
        choice = input("Enter a choice: ")
        if choice == "1":
                message = input("Enter the sentence you want to encrypt: ")                 
                print(encrypt(message.upper()))
                reAsk()
        elif choice == "2":
                message = input("Enter the morse you want to decrypt: ") 
                print(decrypt(message.upper()))
                reAsk()
        else:
                print("That's an oops. Try again by giving a valid input.\n") 
                menu()

menu()
