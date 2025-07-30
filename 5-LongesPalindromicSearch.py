#Buscar el palíndromo más largo en una cadena
texto = "patacas coseicha propia"

def buscarPalindromo(texto):
    palindromo = ""
    maxPalindromo = ""
    #caracteres = set()

    for i in range(1, len(texto)):
        if texto[i-1] == texto[i+1]:
            palindromo += texto[i-1]
            palindromo += texto[i]
            palindromo += texto[i+1]
            if palindromo > maxPalindromo:
                maxPalindromo = palindromo
            return maxPalindromo
print(buscarPalindromo(texto))