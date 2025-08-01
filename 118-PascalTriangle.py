import pandas as pd
while True:
    try:
        filas = int(input("Indique numero de filas: "))
        break
    except ValueError:
        print("Numero invalido")

triangulo = []

def pascal(filas):
    f = [1]
    for fila in range(filas):
        triangulo.append(f)
        f = [1] + [f[i] + f[i+1] for i in range(len(f)-1)] + [1]


    return triangulo

print(pd.DataFrame(pascal(filas)))