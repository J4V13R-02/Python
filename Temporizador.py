import time

while True:
    try:
        tiempo = int(input("Indique el tiempo en segundos"))
        break
    except ValueError:
        print("Valor invalido")

for s in range(0, tiempo):
    time.sleep(1)
    segundos = tiempo % 60
    minutos = (tiempo // 60) % 60
    horas = tiempo // 3600
    print(f"{horas: 02}:{minutos: 02}:{segundos: 02}")
    tiempo -= 1