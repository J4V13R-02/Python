#Se da una cadena, identificar el largo del subarray más largo que contiene sin repetir un caracter.
texto = "abdcadcbadbacdbacccabdcddcabdc"

def busqueda(texto):
    max_subcadena = ""
    subcadena = ""
    caracteres = set()
    izquierda = 0

    for derecha in range(len(texto)):
        while texto[derecha] in caracteres:
            caracteres.remove(texto[izquierda])
            subcadena = subcadena[1:]
            izquierda += 1
        caracteres.add(texto[derecha])
        subcadena += texto[derecha]
        print(subcadena)
        if len(subcadena) > len(max_subcadena):
            max_subcadena = subcadena
    return max_subcadena

print("La cadena más larga es "+ str(busqueda(texto)))
