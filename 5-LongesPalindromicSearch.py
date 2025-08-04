#Buscar el palíndromo más largo en una cadena
class Solution:
    def longestPalindrome(s):
        maxPalindromo = ""
        longitud = 0

        for i in range(len(s)):
            #Impares
            izq, der = i, i
            while izq >= 0 and der < len(s) and s[izq] == s[der]:
                if (der - izq + 1) > longitud:
                    maxPalindromo = s[izq:der + 1]
                    longitud = der - izq + 1
                izq -= 1
                der += 1

            #Pares
            izq, der = i, i + 1
            while izq >= 0 and der < len(s) and s[izq] == s[der]:
                if (der - izq + 1) > longitud:
                    maxPalindromo = s[izq:der + 1]
                    longitud = der - izq + 1
                izq -= 1
                der += 1

        return maxPalindromo

    s = input("Inserte frase: ")
    print(longestPalindrome(s))