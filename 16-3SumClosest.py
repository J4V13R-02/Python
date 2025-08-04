import random

nums = [random.randint(-50, 50) for _ in range(10)]
buscado = int(input("Número a buscar: "))
visto = set()
diferencia_max = 50
mejor = 0
def suma(nums, diferencia_max):
    for i in nums:
       visto.add(i)
       for j in nums:
           if j not in visto:
                objetivo = buscado - (i + j)
                visto.add(j)
                if objetivo in nums:
                    return objetivo
                else:
                    for k in nums:
                        if k not in visto:
                            visto.add(k)
                            diferencia = (objetivo - k)
                            if diferencia < diferencia_max:
                                diferencia_max = diferencia
                                mejor = i + j + k
                                mejor_comb = [i, j, k]
    return mejor, mejor_comb

print(nums)
print(suma(nums, diferencia_max=1000))