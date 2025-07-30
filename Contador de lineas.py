import os

def contar_lineas(directorio):
    total_lineas = 0
    for carpeta_raiz, _, archivos in os.walk(directorio):
        for archivo in archivos:
            if archivo.endswith(".py"):  # Solo contar archivos .py
                ruta_archivo = os.path.join(carpeta_raiz, archivo)
                with open(ruta_archivo, 'r', encoding='utf-8', errors='ignore') as f:
                    lineas = f.readlines()
                    total_lineas += len(lineas)
    return total_lineas

directorio = "C:/Users/javie/PycharmProjects/Python"
print(f"Total de líneas de código Python: {contar_lineas(directorio)}")