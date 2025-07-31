columnas = [1,8,10,2,5,2,8,10,7]
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

print("La capacidad máxima es de " + capacidad(columnas))
                    
