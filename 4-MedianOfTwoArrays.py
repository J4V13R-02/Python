# Calcular la mediana de dos arrays
nums1 = [1, 80, 26, 52, 6, 9]
nums2 = [2, 5, 36, 6, 15]
conjunto = sorted(nums1 + nums2)

def mediana(conjunto):


    if len(conjunto) % 2 == 0:
        valorMediana = (conjunto[len(conjunto) // 2] + conjunto[(len(conjunto) // 2) - 1]) / 2
        return valorMediana
    else:
        valorMediana = conjunto[len(conjunto) // 2]
        return valorMediana

print("La mediana del conjunto " + str(conjunto) + " es " + str(mediana(conjunto)))