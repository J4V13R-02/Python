texto = "PAYPALISHIRING"
numFilas = 3

def zigzag(texto):
    zigzagueado = ""
    for i in range(0, (len(texto)), len(texto)):
        for j in range(i, len(texto), len(texto) // numFilas):
            zigzagueado += texto[j]
    return zigzagueado

print(zigzag(texto))