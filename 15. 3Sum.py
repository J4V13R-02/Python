import random

nums = [random.randint(-5, 5) for _ in range(10)]
conjuntos = []
visto = set()

def suma(nums):
    for i in range (len(nums)):
        for j in range (i+1, len(nums)):
            buscado = -(nums[i] + nums[j])
            for k in range (j+1, len(nums)):
                if buscado == nums[k]:
                    combinacion = tuple(sorted([nums[i], nums[j], buscado]))
                    if combinacion not in visto:
                        conjuntos.append(list(combinacion))
                        visto.add(combinacion)
    return conjuntos
print(nums)
print(suma(nums))