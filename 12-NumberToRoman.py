numero = 2345
romano = ""
def romanizar(numero, romano):
    for i in range(numero // 1000):
        romano += "M"