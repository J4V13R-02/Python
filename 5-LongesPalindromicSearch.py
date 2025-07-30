#Buscar el palíndromo más largo en una cadena
texto = "patapcas coseicha propia"

def buscarPalindromo(texto):
    maxPalindromo = ""

    for i in range(1, len(texto) - 1):
        if texto[i - 1] == texto[i + 1]:
            palindromo = texto[i]
            izquierda = i - 1
            derecha = i + 1

            while izquierda >= 0 and derecha < len(texto) and texto[izquierda] == texto[derecha]:
                palindromo = texto[izquierda] + palindromo + texto[derecha]
                izquierda -= 1
                derecha += 1

            if len(palindromo) > len(maxPalindromo):
                maxPalindromo = palindromo

    return maxPalindromo

print(buscarPalindromo(texto))