nums = [-1,0,1,2,-1,-4]
conjuntos = []
visto = {}

def sum(nums):
    combinación = []
    for i in range (len(nums)):
        for j in range (i+1, len(nums)):
            buscado = (nums[i] + nums[j]) * -1
            if buscado in nums and combinacion not in visto:
                combinacion = sorted([nums[i], nums[j], buscado])
                conjuntos.append(combinacion)
                visto.append = combinacion
    return conjuntos

print(sum(nums))