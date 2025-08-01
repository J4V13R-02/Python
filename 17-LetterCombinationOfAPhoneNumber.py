teclado = {
    2: ["a", "b", "c"],
    3: ["d", "e", "f"],
    4: ["g", "h", "i"],
    5: ["j", "k", "l"],
    6: ["m", "n", "o"],
    7: ["p", "q", "r"],
    8: ["s", "t", "u", "v"],
    9: ["w", "x", "y", "z"]

}
digitos = int(input("Inserte dos numeros: "))
def combinaciones(digitos, teclado):
    s = []
    num_a = digitos % 10
    num_b = digitos // 10
    for i in teclado[num_a]:
        for j in teclado[num_b]:
            s.append(f"{i + j}")
    return s
print(f"Combinaciones para {digitos}: {combinaciones(digitos, teclado)}")