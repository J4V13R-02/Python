while True:
    try:
        numero = str(int(input("Inserte número ")))

        def esPalindromo(numero):
            inversaNumero = numero[::-1]
            if inversaNumero == numero:
                return True
            else:
                return False

        if esPalindromo(numero) == True:
            print(numero + " es palindromo.")
        elif numero[0] == "-":
            print(numero + " no es palindromo, porque es negativo.")
        else:
            print(numero + " no es palindromo")
    except ValueError:
        print("Contiene simbolos que no son números o el signo negativo.")


