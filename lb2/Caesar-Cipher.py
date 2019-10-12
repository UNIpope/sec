# encrypt and decrypt a text using a simple algorithm of offsetting the letters

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
offset = 17
f = open("caesarText.txt", 'r')
cipher = f.read()
cipher = filter(str.isalpha, cipher.upper())

def decrypt(n, ciphertext):
    """Decrypt the string and return the plaintext"""
    result = ""

    for letter in ciphertext:
        if letter in alpha:  # if the letter is actually a letter
            # find the corresponding ciphertext letter in the alphabet
            letter_index = (alpha.find(letter) - n) % len(alpha)

            result = result + alpha[letter_index]
        else:
            result = result + letter

    return result

decrypted = decrypt(offset, cipher)
print('Decrypted:', decrypted)
