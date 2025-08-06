fibo = [0, 1, 1]
limite = 100
mejor_phi = 0

def fibonacci(i, fibo, limite):
    fibo.append(fibo[i] + fibo[i - 1])
    return fibo[i + 1]

def phi(i, fibo, limite):
    mejor_phi = fibo[i] / fibo[i - 1]
    return mejor_phi

for i in range(2, limite):
    print(f"Posicion {i} Para: {fibonacci(i, fibo, limite)} phi es igual a: {phi(i, fibo, limite)}")