s = input("Inserte texto S: ")
p = input("Inserte texto P: ")

caracteres = []

def comparar(s, p):
    if len(s) != len(p):
        print("El largo no coincide")
        return False

    for i in range(len(s)):
        if s[i] == p[i]:
            continue
        elif s[i] == "*" or p[i] == "*":
            continue
        elif s[i] == "-" or p[i] == "-":
            ch = s[i] if s[i] != "-" else p[i]
            if ch in caracteres:
                continue
            else:
                caracteres.append(ch)
                continue
        else:
            return False
    return True

if comparar(s, p):
    print("Las expresiones coinciden.")
else:
    print("Las expresiones no coinciden.")

print("Caracteres especiales guardados:", caracteres)
