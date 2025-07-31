teclado = {
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz"
}

def combinaciones(digitos, teclado):
    if not digitos:
        return []
    for d in digitos:
        if d not in teclado:
            return []
    resultado = [""]
    for d in digitos:
        letras = teclado[d]
        nuevo = []
        for prefijo in resultado:
            for letra in letras:
                nuevo.append(prefijo + letra)
        resultado = nuevo
    return resultado

while True:
    entrada = input("Inserte dos cifras (2–9, sin espacios), o 'salir' para terminar: ").strip()
    if entrada.lower() == "salir":
        break
    if len(entrada) != 2 or any(ch not in teclado for ch in entrada):
        print("Debe insertar un número de dos cifras válidas entre 2 y 9.")
        continue
    combos = combinaciones(entrada, teclado)
    print(f"Combinaciones para {entrada}: {combos}")