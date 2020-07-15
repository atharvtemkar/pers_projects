def encaesar():
    plain = input('Enter the plain text: ')
    k = int(input('Enter the key: '))
    result = ""
    for i in range(len(plain)): 
        char = plain[i]
        if (char.isupper()): 
            result += chr((ord(char) + k-65) % 26 + 65)
        else: 
            result += chr((ord(char) + k-97) % 26 + 97)
		
    print ("Text : ",plain)
    print ("Shift : ",str(k))
    print ("Cipher: ",result)

def decaesar():
    cipher = input('Enter the plain text: ')
    k = int(input('Enter the key: '))
    k=26-k
    result = ""
    for i in range(len(cipher)):
        char = cipher[i]
        if (char.isupper()): 
            result += chr((ord(char) + k-65) % 26 + 65)
        else: 
            result += chr((ord(char) + k-97) % 26 + 97)

    print ("Cipher: ",cipher)
    print ("Shift : ",str(k))
    print ("Cipher: ",result)

def atbash():
    atbash_values = {'A':'Z', 'B':'Y', 'C':'X', 'D':'W', 'E':'V', 'F':'U', 'G':'T', 'H':'S', 'I':'R', 'J' : 'Q', 'K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L', 'P' : 'K', 'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G', 'U' : 'F', 'V':'E', 'W':'D', 'X':'C', 'Y':'B', 'Z':'A'}
    user_in = input('Enter the plain text: ')
    user_in = user_in.upper()
    user_out = ""
    for i in user_in:
        if(i != ' '): 
            user_out += atbash_values[i] 
        else: 
            user_out += ' '
    
    print ("Input: ",user_in)
    print ("Output: ",user_out)

def vernam():
    plain = input('Enter the plain text: ')
    plain = plain.upper()
    key = input('Enter the key equal to plain text: ')
    key = key.upper()
    cipher = ""
    if (len(plain)==len(key)):
        for i in range(len(plain)):
            char1 = plain[i]
            char2 = key[i]
            asciical1 = ord(char1)-65
            asciical2 = ord(char2)-65
            asciisum = asciical1 + asciical2
            if (asciisum >= 26):
                asciisum = asciisum - 26
                cipher += chr(asciisum + 65)

            else:
                cipher += chr(asciisum + 65)

    else:
        print ("Plain text and keyword are not equal in size.")

    print ("Plain Text: ",plain)
    print ("Keyword: ",key)
    print ("Cipher Text: ",cipher)
    

print("Choose a method for encryption: ")
print("1. Encrypt Caesar Cipher")
print("2. Decrypt Caesar Cipher")
print("3. Encrypt Atbash Cipher")
print("4. Decrypt Atbash Cipher")
print("5. Encrypt Vernam Cipher")
#print("6. Decrypt Vernam Cipher")

choice = int(input('Enter the choice: '))
if choice==1:
    encaesar()
                            
elif (choice == 2):
    decaesar()
    
elif choice == 3:
    atbash()
    
elif choice == 4:
    atbash()

elif choice == 5:
    vernam()

else:
    print("Invalid choice")
