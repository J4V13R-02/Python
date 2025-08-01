try:
    filas = int(input("Indique numero de filas: "))
except ValueError:
    print("Numero invalido")

triangulos = []

def pascal(filas):
    f = [1]
    for fila in range(filas):
        for i in range(len(f)):
            if i+1 <= len(f):
                f.append((f[i] + (f[i+1])))
            else:
                f.append((f[i]))
        triangulos.append(list(f))
    return triangulos

print(pascal(filas))