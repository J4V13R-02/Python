# Reto 1 de LeetCode
# Dar un array de números y un objetivo. La función debe encontrar en el array dos números que den como suma el objetivo.

nums = [2, 7, 11, 13]
target = 9

# Mi enfoque será restar al target los números, de uno en uno. Comprobar si la resta aparece en el array.

for i in range(len(nums)):
    buscado = target - nums[i]
    print(target + " es la suma de " + nums[i] + " y " + buscado)
    print("Buscando " + buscado + " en la lista...")
    for n in range(len(nums)):
        if buscado == nums[n]:
            suma = [nums[i], buscado]
            print(suma)