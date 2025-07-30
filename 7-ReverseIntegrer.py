integ = 345

def reverse(integ):

    numeroInvertido = str(abs(integ))[::-1]
    numeroInvertido = int(numeroInvertido)
    if integ < 0:
        numeroInvertido = numeroInvertido * -1
        return numeroInvertido
    else:
        return numeroInvertido
print(str(reverse(integ)))