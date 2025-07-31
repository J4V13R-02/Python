import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


columnas = [random.randint(1, 10) for _ in range(10)]
columna_a = ""
columna_b = ""

def capacidad(columnas):
    max_deposito = 0
    deposito = 0
    for i in range(len(columnas)-1):
        for j in range(i+1, len(columnas)):
            if columnas[i] > columnas[j]:
                deposito = columnas[j] * (j-i)
            else:
                    deposito = columnas[i] * (j-i)
            if deposito > max_deposito:
                max_deposito = deposito
                columna_a = i+1
                columna_b = j+1

    return (str(max_deposito) + " formado por las columnas " + str(columna_a) + " y " + str(columna_b))

print(str(columnas))
print("La capacidad máxima es de " + capacidad(columnas))
etiquetas = [f"{i}" for i in range(len(columnas))]
plt.figure()
plt.bar(etiquetas, columnas)
plt.show()
                    
