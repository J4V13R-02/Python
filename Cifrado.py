import random
import string

chars = string.ascii_letters + string.digits
chars = list(chars)
crypt = chars.copy()

random.shuffle(crypt)

texto = input("Escriba su frase: ")
cifrado = ""

def crypher(texto, chars, crypt, cifrado):
    for char in texto:
        index = chars.index(char)
        cifrado += crypt[index]
    return cifrado

print(f" el texto cifrado es: {crypher(texto, chars, crypt, cifrado)}")