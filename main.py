from EncryptV2 import encrypt
from DecryptV2 import decrypt
import Conversions

f = open("pad.bin")
pad = f.read()

# Shows how many characters are left in the pad
print("left in pad: {0}".format(len(pad)))

#plaintext message
p_text = input("Message: ")

#Generates and prints cipher binary
c_binary = encrypt(p_text, pad)
print("Cipher binary: {0}".format(c_binary))

#Decrypts cipher binary and prints message binary
d_text = decrypt(c_binary, pad)
print("Decrypted binary: {0}".format(d_text))

#decoded binary
print("Decrypted message: {0}".format(Conversions.toText(d_text)))