# Se da una lista de numeros de una cifra. sumar los números dos a dos en orden inverso.
# Si suman más de 9, se toma el dígito de las unidades.

l1 = [2, 4, 3, 8]
l2 = [5, 6, 4, 9]

def addTwoNumbers(l1, l2):
    suma = 0
    for numero in range(len(l1)):
        suma += (l1[numero] + l2[numero]) * (10**numero)
    return suma

print(str(addTwoNumbers(l1, l2)) + "es la suma")