# Se da una lista de numeros de una cifra. sumar los números dos a dos en orden inverso.
# Si suman más de 9, se toma el dígito de las unidades.

l1 = [2, 4, 3]
l2 = [5, 6, 4]

def addTwoNumbers(l1, l2):
    for numero in range(l1):
        suma = l1(numero) + l2(numero)
        return suma * (10**numero) 
    numero +=1

print(addTwoNumbers)